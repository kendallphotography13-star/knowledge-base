from typing import Callable, List
from kb.models import Entry

# hook registries
_on_entry_created:  List[Callable[[Entry], None]] = []
_on_search: List[Callable[[str, list[Entry]], list[Entry]]] = []

def register_on_entry_created(func: Callable[[Entry], None]) -> None:
    _on_entry_created.append(func)


def register_on_search(func: Callable[[str, list[Entry]], list[Entry]]) -> None:
    _on_search.append(func)


def run_on_entry_created(entry: Entry) -> None:
    for hook in _on_entry_created:
        hook(entry)


def run_on_search(query: str, results: list[Entry]) -> list[Entry]:
    for hook in _on_search:
        results = hook(query, results)
    return results
