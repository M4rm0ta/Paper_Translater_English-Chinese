# Full-paper translation and PDF quality guide

## Source preparation

- Record title, authors, source file/URL, version, page count, extracted reading order, figure/table count, numbered equations and references. Count unnumbered display math as well. Read two-column PDFs in the correct order; visually review extracted text, hyphenation and OCR confidence. Scan-only PDFs require OCR plus comparison with page images.
- Download public author sources only when useful and allowed; compare with the provided version. TeX archives may contain commands or external files: inspect as data and avoid executing document code. A PDF page is authoritative when source versions differ.
- Keep block IDs stable. Store each block's type, page, original, translation, and, for image assets, file path and extraction location. Track source-to-output page mapping. The source map must not claim a block is translated or checked until this has actually happened.

## Translation and math

- Retain the structure and full reasoning of each paragraph, including hypotheses, exceptions, experimental settings, symbols and citation markers. Translate figure captions and table content; preserve bibliographic metadata and translate titles when requested. Record uncertain text and omitted metadata explicitly.
- Reuse exact mathematical expressions in English and Chinese. MathJax or a verified local TeX pipeline can typeset inline/display expressions; render errors and unsupported commands are blockers for a claim of completed math. Author-source macros may need safe expansion. Watch look-alikes such as tau/T, phi/varphi, Greek nu/v, and calligraphic/ordinary letters.
- Where a formula must be extracted as an image, include the full equation, number and all glyphs at sufficient resolution. Inspect against the original. Avoid clipped surrounding text; disclose that image equations are not editable LaTeX. Original-page inclusion may aid comparison but does not substitute for a complete translation.
- Do not silently correct a suspicious formula or scientific statement. Preserve the original, clearly label an issue as a translator's observation, and ground it in its source page; cite independent evidence before calling it a confirmed erratum.

## Layout and visual QA

- The output PDF should have readable text, Chinese fonts, stable source references and original/translation alignment. Equations, captions and their figures should remain together when feasible. Preserve source page references; a translated paragraph may span pages when unavoidable without losing text.
- Figure crops need visual checks of all sides and subpanels, including lowermost/leftmost ticks, axis titles and exponents, legends, panel identifiers and annotations. Check tables for every row, column and footnote. Cross-column figures require complete bounds.
- Render every final output page using an available PDF renderer (e.g. Poppler), inspect contact sheets, and inspect detailed pages with dense formulas or figures. Re-render and recheck affected pages after any change. Check for missing glyphs, text collisions, clipped ink, tiny formulas, truncated hyperlinks and cut figures.
- If rendering tools are missing or the output cannot be checked, disclose the precise limitation and keep the output marked draft. Text extraction and matching block IDs alone cannot prove translation correctness, image completeness or visual quality.

## Privacy, dependencies and handoff

- Work locally by default. Do not upload a paper to a remote OCR/translation service without appropriate user authorization. Do not redistribute third-party articles or figures merely because they are accessible online.
- Prefer existing installed PDF and math tools. Optional choices include Poppler for page rendering, `pdfplumber` or `pypdf` for extraction, ReportLab for PDF generation and MathJax for LaTeX typesetting. These tools have their own dependencies and licenses; do not assume installation, TeX engines or particular OS fonts.
- Final handoff: link the deliverable, explain layout and whether math is editable, report actual checks and remaining uncertainties, and mention any source issue separately from the translation. Preserve user edits and prior outputs.

