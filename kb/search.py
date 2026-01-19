from typing import List

from kb.database import get_connection
from kb.models import Entry
from kb.storage import _row_to_entry


def search_entries(keyword: str) -> List[Entry]:
    pattern = f"%{keyword}%"

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT * FROM entries
        WHERE title LIKE ? OR content LIKE ?
        ORDER BY id DESC
        """,
        (pattern, pattern),
    )

    rows = cur.fetchall()
    conn.close()

    return [_row_to_entry(row) for row in rows]
