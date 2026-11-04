# Paper Translator English–Chinese

一个面向科研论文的英文—中文全文对照翻译 skill。它帮助 AI 助手保留原文、中文、公式、图表、页码及参考文献，并在需要时制作可核对的 PDF。

## 包含什么

`paper-translator/SKILL.md` 是 skill 入口；`references/workflow.md` 包含公式、图表与 PDF 核验细节；`scripts/check_reader.py` 检查来源映射和图片链接。脚本不翻译论文，也不能代替人工检查数学符号、译文准确性或 PDF 排版。

## 使用

将 `paper-translator/` 放入所用 AI 助手支持的 skills 目录，并确保该助手可以读取其中的 `SKILL.md`。不同产品的安装与发现方式可能不同，请以对应产品文档为准。然后提供论文 PDF 或可访问的论文链接，例如：

> 使用 paper-translator 把这篇论文全文翻译为中英对照 PDF；公式保留 LaTeX，检查所有图的坐标轴和图例。

助手应先确认源文件、版本与输出格式，再按照 skill 执行全文翻译、整理来源映射、核对公式和图表。项目输出通常包括 `paper.md`、`source_map.json`、`translation_notes.md`、`assets/`，按需另生成 PDF。阅读顺序、公式密集程度和论文长度会影响处理时间。

如需检查结果的基础结构，可运行：

```sh
python paper-translator/scripts/check_reader.py path/to/project
```

该检查只验证文件存在、JSON 块 ID 和图片路径等基础结构；公式是否正确、图表是否完整及版面是否可读仍需实际核对。

## 公式与图表

优先使用与用户 PDF 版本一致、经验证的作者 LaTeX 源码；无可靠源码时可保留原 PDF 的排版公式，并说明其不是可编辑 LaTeX。图表须保留坐标轴、刻度、图例和所有子图，PDF 交付前逐页渲染检查。

本仓库不附带论文、译文、专有字体或第三方工具。PDF 提取、OCR、数学排版及生成可能需要额外工具，具体取决于运行环境。处理非公开论文时，使用第三方服务前应取得适当授权；分享论文或译文前请确认权利。

## 许可证

本项目采用 [MIT License](LICENSE)。第三方工具和论文各自适用其原有条款。

