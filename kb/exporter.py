from __future__ import annotations

import json
import re
from pathlib import Path
from typing import List, Literal

from kb.models import Entry


def _slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text or "untitled"


def _to_markdown(entry: Entry) -> str:
    return (
        f"# {entry.title}\n\n"
        f"- id: {entry.id}\n"
        f"- type: {entry.entry_type}\n"
        f"- created_at: {entry.created_at}\n"
        f"- updated_at: {entry.updated_at}\n\n"
        f"---\n\n"
        f"{entry.content}\n"
    )


def export_entries(
    entries: List[Entry],
    out_dir: str,
    fmt: Literal["md", "json"] = "md",
) -> int:
    out_path = Path(out_dir).resolve()
    out_path.mkdir(parents=True, exist_ok=True)

    if fmt == "json":
        data = [
            {
                "id": e.id,
                "title": e.title,
                "content": e.content,
                "type": e.entry_type,
                "created_at": e.created_at.isoformat(),
                "updated_at": e.updated_at.isoformat(),
            }
            for e in entries
        ]

        (out_path / "entries.json").write_text(
            json.dumps(data, indent=2), encoding="utf-8"
        )
        return len(entries)

    for e in entries:
        filename = f"{e.id:05d}-{_slugify(e.title)}.md"
        (out_path / filename).write_text(_to_markdown(e), encoding="utf-8")

    return len(entries)
