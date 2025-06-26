from vault_utils import init_db
from Helix_Core import PrometheusCodex  # Ensure filename matches exactly
from codex_bridge import CodexBridge
from whispering_archive import WhisperingArchive
from InjectedLegacy.CatoPrime.Caleonprime.caleon_core import CaleonPrime

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

if __name__ == "__main__":
    main()
