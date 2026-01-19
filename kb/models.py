from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Entry:
    id: Optional[int]
    title: str
    content: str
    entry_type: str
    created_at: datetime
    updated_at: datetime