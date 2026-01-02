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
### DOCX
```
uvx --from pypandoc-binary python scripts/convert_markdown.py input.md --to docx
```

### PDF
```
uvx --from pypandoc-binary python scripts/convert_markdown.py input.md --to pdf
```

### With options
```
uvx --from pypandoc-binary python scripts/convert_markdown.py input.md --to docx \
  --reference-doc template.docx \
  --toc \
  --metadata title="My Doc"
```

## Install as a Skill
Symlink the skill folder into your Codex skills directory:
```
ln -s markdown-to-docs-pdf ~/.codex/skills/markdown-to-docs-pdf
```

If you prefer an absolute path:
```
ln -s /absolute/path/to/convert-markdown-to-docs-or-pdf/markdown-to-docs-pdf \
  ~/.codex/skills/markdown-to-docs-pdf
```

## Notes
- `--pdf-engine` can be passed if you need a specific Pandoc engine (e.g., `wkhtmltopdf`, `tectonic`).
- If Pandoc is already installed, you can run the script with `python3` directly.
# convert-markdown-to-docx-or-pdf-agent-skill
