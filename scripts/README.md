# Markdown → PDF

Convert a `.md` file to `.pdf`.

## Install dependencies

```bash
brew install pango cairo gdk-pixbuf libffi
```

## Setup

From the root of the repository:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements.txt
```

## Usage

```bash
python scripts/md_to_pdf.py INPUT.md OUTPUT.pdf [--title "My Title"] [--help]
```

Example:

```bash
python scripts/md_to_pdf.py src/tp/tp.md 05_tp.pdf --title "TP - Coding with IA"
```

## Reactivate environment later

```bash
source .venv/bin/activate
```
