# Knowledge Base (CLI)

A local-first command-line knowledge base built with Python and SQLite.

This tool is for developers who are constantly learning new tools, APIs, and frameworks and want a fast, simple place to store and retrieve notes — without cloud lock-in or heavy UIs.

## Why This Exists

Over time, notes end up scattered across:
- Notion
- Apple Notes
- Markdown files
- Browser bookmarks

This project is a focused alternative:
- No sync
- No accounts
- No graphs
- No WYSIWYG
- Just fast capture and retrieval from the command line

## Features

- Add notes from the CLI
- List all entries
- View a specific entry
- Search by keyword
- Delete entries
- Export notes to Markdown
- Local SQLite database (your data stays on your machine)

## Install

```bash
git clone https://github.com/kendallphotography13-star/knowledge-base.git
cd knowledge-base
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

