# Markdown to DOCX/PDF Skill

A skill that converts Markdown files to DOCX or PDF using Pandoc via a bundled Python script. Designed to run with `uvx` + `pypandoc-binary` so Pandoc is available without a system install.

## Repository Layout
```
markdown-to-docx-pdf/
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
ln -s markdown-to-docx-pdf ~/.codex/skills/markdown-to-docx-pdf
```

Or with absolute path:
```
ln -s /absolute/path/to/convert-markdown-to-docx-or-pdf/markdown-to-docx-pdf \
  ~/.codex/skills/markdown-to-docx-pdf
```

### For Claude Code
```
ln -s markdown-to-docx-pdf ~/.claude/skills/markdown-to-docx-pdf
```

Or with absolute path:
```
ln -s /absolute/path/to/convert-markdown-to-docx-or-pdf/markdown-to-docx-pdf \
  ~/.claude/skills/markdown-to-docx-pdf
```

### For Qwen CLI
```
ln -s markdown-to-docx-pdf ~/.qwen/skills/markdown-to-docx-pdf
```

Or with absolute path:
```
ln -s /absolute/path/to/convert-markdown-to-docx-or-pdf/markdown-to-docx-pdf \
  ~/.qwen/skills/markdown-to-docx-pdf
```

### For iFlow
```
ln -s markdown-to-docx-pdf ~/.iflow/skills/markdown-to-docx-pdf
```

Or with absolute path:
```
ln -s /absolute/path/to/convert-markdown-to-docx-or-pdf/markdown-to-docx-pdf \
  ~/.iflow/skills/markdown-to-docx-pdf
```

## Notes
- PDF conversion uses LaTeX.
# convert-markdown-to-docx-or-pdf-agent-skill
