# Markdown to Docs/PDF Skill

A Codex skill that converts Markdown files to DOCX or PDF using Pandoc via a bundled Python script. Designed to run with `uvx` + `pypandoc-binary` so Pandoc is available without a system install.

## Features
- Convert `.md` to `.docx` or `.pdf`
- Optional DOCX template via `--reference-doc`
- Optional TOC via `--toc`
- Metadata via `--metadata key=value`

## Repository Layout
```
markdown-to-docs-pdf/
  SKILL.md
  scripts/
    convert_markdown.py
```

## Usage

### Natural Language Prompts

Simply tell the AI what you want:

```
把这个markdown给我搞成pdf
把这个markdown转换成word文档
帮我把这个md文件导出为pdf，带上目录
```

## Install as a Skill

### For Codex
```
ln -s markdown-to-docs-pdf ~/.codex/skills/markdown-to-docs-pdf
```

Or with absolute path:
```
ln -s /absolute/path/to/convert-markdown-to-docs-or-pdf/markdown-to-docs-pdf \
  ~/.codex/skills/markdown-to-docs-pdf
```

### For Claude Code
```
ln -s markdown-to-docs-pdf ~/.claude/skills/markdown-to-docs-pdf
```

Or with absolute path:
```
ln -s /absolute/path/to/convert-markdown-to-docs-or-pdf/markdown-to-docs-pdf \
  ~/.claude/skills/markdown-to-docs-pdf
```

### For Qwen CLI
```
ln -s markdown-to-docs-pdf ~/.qwen/skills/markdown-to-docs-pdf
```

Or with absolute path:
```
ln -s /absolute/path/to/convert-markdown-to-docs-or-pdf/markdown-to-docs-pdf \
  ~/.qwen/skills/markdown-to-docs-pdf
```

### For iFlow
```
ln -s markdown-to-docs-pdf ~/.iflow/skills/markdown-to-docs-pdf
```

Or with absolute path:
```
ln -s /absolute/path/to/convert-markdown-to-docs-or-pdf/markdown-to-docs-pdf \
  ~/.iflow/skills/markdown-to-docs-pdf
```

## Notes
- `--pdf-engine` can be passed if you need a specific Pandoc engine (e.g., `wkhtmltopdf`, `tectonic`).
- If Pandoc is already installed, you can run the script with `python3` directly.
# convert-markdown-to-docx-or-pdf-agent-skill
