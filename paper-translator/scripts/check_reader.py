#!/usr/bin/env python3
"""Check source-map structure and local Markdown image links; no PDF rendering."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote


def check(base: Path) -> list[str]:
    issues = []
    md = base / 'paper.md'
    source = base / 'source_map.json'
    notes = base / 'translation_notes.md'
    for path in (md, source, notes):
        if not path.is_file():
            issues.append(f'missing: {path.name}')
    if md.is_file():
        text = md.read_text(encoding='utf-8')
        for target in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text):
            if target.startswith(('https://', 'http://', 'data:')):
                continue
            path = base / unquote(target.split('#', 1)[0].strip('<>'))
            if not path.is_file():
                issues.append(f'missing image: {target}')
    if source.is_file():
        try:
            data = json.loads(source.read_text(encoding='utf-8'))
            blocks = data.get('blocks') if isinstance(data, dict) else None
            if not isinstance(blocks, list) or not blocks:
                issues.append('source_map.json must have a nonempty blocks list')
            else:
                ids = [b.get('id') for b in blocks if isinstance(b, dict)]
                if len(ids) != len(blocks) or any(not isinstance(i, str) or not i for i in ids):
                    issues.append('each block needs a nonempty string id')
                elif len(ids) != len(set(ids)):
                    issues.append('duplicate block IDs')
                for block in blocks:
                    if isinstance(block, dict) and block.get('asset'):
                        if not (base / block['asset']).is_file():
                            issues.append(f"missing asset for {block.get('id')}: {block['asset']}")
        except (ValueError, OSError) as error:
            issues.append(f'invalid source map: {error}')
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    args = parser.parse_args()
    errors = check(args.project)
    for error in errors:
        print(f'ERROR: {error}', file=sys.stderr)
    if not errors:
        print('Structural checks passed. Translation accuracy and visual layout require manual review.')
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())

