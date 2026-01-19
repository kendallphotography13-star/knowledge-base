from kb.hooks import register_on_entry_created

def log_entry(entry):
    print(f"[LOG] New entry created: {entry.title}")

register_on_entry_created(log_entry)
