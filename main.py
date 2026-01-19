from kb.database import initialize_database
from kb.storage import (
    add_entry,
    get_all_entries,
    get_entry_by_id,
    delete_entry,
)
from kb.search import search_entries
from kb.exporter import export_entries


def print_entry(entry):
    print(f"\n[{entry.id}] {entry.title} ({entry.entry_type})")
    print(entry.content)
    print("-" * 40)


def main():
    initialize_database()
    print("Knowledge Base CLI — type 'help'")

    while True:
        cmd = input("\n> ").strip()

        # ---------- HELP ----------
        if cmd == "help":
            print(
                """
add                 Add entry
list                List entries
view <id>           View entry
search <term>       Search entries
delete <id>         Delete entry
export <dir>        Export to markdown
export <dir> --json Export to JSON
quit                Exit
"""
            )

        # ---------- ADD ----------
        elif cmd == "add":
            title = input("Title: ").strip()
            if not title:
                print("Cancelled (empty title).")
                continue

            content = input("Content: ").strip()
            if not content:
                print("Cancelled (empty content).")
                continue

            entry_type = input("Type [note/code/link]: ").strip() or "note"

            entry = add_entry(title, content, entry_type)
            print(f"✔ Added entry #{entry.id}")

        # ---------- LIST ----------
        elif cmd == "list":
            entries = get_all_entries()
            if not entries:
                print("No entries found.")
            for e in entries:
                print(f"[{e.id}] {e.title}")

        # ---------- VIEW ----------
        elif cmd.startswith("view"):
            parts = cmd.split()

            if len(parts) != 2 or not parts[1].isdigit():
                print("Usage: view <id>")
                continue

            entry = get_entry_by_id(int(parts[1]))
            if entry:
                print_entry(entry)
            else:
                print("Entry not found.")

        # ---------- SEARCH ----------
        elif cmd.startswith("search"):
            parts = cmd.split(maxsplit=1)

            if len(parts) != 2:
                print("Usage: search <term>")
                continue

            results = search_entries(parts[1])
            if not results:
                print("No results.")
            for e in results:
                print(f"[{e.id}] {e.title}")

        # ---------- DELETE ----------
        elif cmd.startswith("delete"):
            parts = cmd.split()

            if len(parts) != 2 or not parts[1].isdigit():
                print("Usage: delete <id>")
                continue

            if delete_entry(int(parts[1])):
                print("✔ Entry deleted.")
            else:
                print("Entry not found.")

        # ---------- EXPORT ----------
        elif cmd.startswith("export"):
            parts = cmd.split()

            if len(parts) < 2:
                print("Usage: export <dir> [--json]")
                continue

            out_dir = parts[1]
            fmt = "json" if "--json" in parts else "md"

            entries = get_all_entries()
            if not entries:
                print("No entries to export.")
                continue

            count = export_entries(entries, out_dir, fmt)
            print(f"✔ Exported {count} entries.")

        # ---------- QUIT ----------
        elif cmd == "quit":
            print("Goodbye.")
            break

        # ---------- UNKNOWN ----------
        else:
            print("Unknown command. Type 'help'.")


if __name__ == "__main__":
    main()
