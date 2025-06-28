from vault_utils import init_db
from Helix_Core import PrometheusCodex  # Ensure filename matches exactly
from codex_bridge import CodexBridge
from whispering_archive import WhisperingArchive
from InjectedLegacy.CatoPrime.Caleonprime.caleon_core import CaleonPrime
from fastapi import APIRouter, HTTPException
from cali.vault.vaultkeeper import load_memory_vault, save_memory_vault
from cali.vault.reconciliation import reconcile_entries, save_reconciled_summary
import uuid
from datetime import datetime

router = APIRouter()

def main():
    # Initialize the database (ensure idempotency in init_db)
    init_db()

    # Initialize core components
    codex = PrometheusCodex()
    bridge = CodexBridge(codex)
    archive = WhisperingArchive()

    # Execute actions
    bridge.inquire_truth("origin")
    bridge.pulse_resonance()
    bridge.harmonic_sync("bonding")

    # Log to archive
    archive.log(bridge.echo_log, actor="Cali")

    # Output song
    print("\n🌀 Echo Memory Verse:")
    print(bridge.sing_back())
    caleon = CaleonPrime()
    print(str(caleon))  # Optional, will show she's online  
    print("\n🕊️ Whispered Thread Summary:")
    latest = archive.latest()
    if latest:
        print(f"{latest['thread_id']} | {latest['glyph_imprint']} | {latest['summary_poem']}")

    # Example usage (replace with your actual logic)
    print("Prometheus Prime system initialized.")
    # You can add more startup logic here as needed

@router.post("/vault/{vault_id}/reconcile")
def reconcile_vault_route(vault_id: str):
    vault = load_memory_vault(vault_id)
    if not vault:
        raise HTTPException(status_code=404, detail="Vault not found.")

    if not vault or "entries" not in vault:
        return {"status": "error", "message": "Vault not found or malformed."}

    entries = vault["entries"]
    unique_fragments = {}

    for e in entries:
        fingerprint = e["content"].lower().strip()
        if fingerprint not in unique_fragments:
            unique_fragments[fingerprint] = e

    synthesized = list(unique_fragments.values())
    synthesized.sort(key=lambda x: x.get("importance", 1.0), reverse=True)

    archive_id = str(uuid.uuid4())
    summary = {
        "archive_id": archive_id,
        "synthesized_count": len(synthesized),
        "timestamp": datetime.utcnow().isoformat(),
        "entries": synthesized[:10]  # Only keep top 10 for now
    }

    # Save to vault as new reconciled summary
    vault["reconciled"] = summary
    save_memory_vault(vault_id, vault)

    return {"status": "ok", "summary": summary}

if __name__ == "__main__":
    main()
