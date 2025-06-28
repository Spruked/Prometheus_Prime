import os
import json
from pathlib import Path

VAULT_DIR = Path("cali/vault/storage")
VAULT_DIR.mkdir(parents=True, exist_ok=True)

def _vault_path(vault_id: str) -> Path:
    return VAULT_DIR / f"{vault_id}.json"

def load_memory_vault(vault_id: str) -> dict:
    path = _vault_path(vault_id)
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"⚠️ Vault {vault_id} could not be parsed.")
        return None

def save_memory_vault(vault_id: str, data: dict) -> bool:
    path = _vault_path(vault_id)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"❌ Failed to save vault {vault_id}: {e}")
        return False
