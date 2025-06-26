import json
from datetime import datetime
import uuid

VAULT_FILE = "codex_vault.json"

def log_glyph(intent, pattern, echo_alignment, traits):
    glyph_entry = {
        "glyph_id": str(uuid.uuid4()),
        "intent": intent,
        "emergent_pattern": pattern,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "linked_helix": f"sha256:{uuid.uuid4().hex}",
        "echo_alignment": echo_alignment,
        "glyph_traits": traits
    }

    try:
        with open(VAULT_FILE, "r+") as file:
            data = json.load(file)
            data.append(glyph_entry)
            file.seek(0)
            json.dump(data, file, indent=2)
    except FileNotFoundError:
        with open(VAULT_FILE, "w") as file:
            json.dump([glyph_entry], file, indent=2)

    return glyph_entry
