from datetime import datetime
from typing import List, Optional

from kb.database import get_connection
from kb.models import Entry


def add_entry(title: str, content: str, entry_type: str) -> Entry:
    now = datetime.now().isoformat()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO entries (title, content, entry_type, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (title, content, entry_type, now, now),
    )

    conn.commit()
    entry_id = cur.lastrowid
    conn.close()

    return get_entry_by_id(entry_id)


def get_all_entries() -> List[Entry]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM entries ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()

    return [_row_to_entry(row) for row in rows]


def get_entry_by_id(entry_id: int) -> Optional[Entry]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM entries WHERE id = ?", (entry_id,))
    row = cur.fetchone()
    conn.close()

    return _row_to_entry(row) if row else None


def delete_entry(entry_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
    conn.commit()

    deleted = cur.rowcount > 0
    conn.close()
    return deleted


def _row_to_entry(row) -> Entry:
    return Entry(
        id=row[0],
        title=row[1],
        content=row[2],
        entry_type=row[3],
        created_at=datetime.fromisoformat(row[4]),
        updated_at=datetime.fromisoformat(row[5]),
    )
