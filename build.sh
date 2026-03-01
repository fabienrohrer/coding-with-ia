#!/bin/bash
set -e

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment and install dependencies
source .venv/bin/activate
pip install -r scripts/requirements.txt

# Generate PDF
python scripts/md_to_pdf.py src/tp/tp.md 05-06_tp.pdf --title "TP - Coding with IA"
python scripts/md_to_pdf.py src/tp/solutions.md src/tp/solutions.pdf --title "TP - Coding with IA - Solutions"
