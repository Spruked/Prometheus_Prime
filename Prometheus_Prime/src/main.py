# main.py

from cali.vault.vaultkeeper import VaultKeeper
from cali.vault.reconciliation import reconcile_entries

def main():
    # Initialize the vault manager
    vault_keeper = VaultKeeper()

    # Load the vault (this could be from a file or database)
    vault = vault_keeper.load_vault()

    # Check if the vault is valid
    if not vault:
        print("Error: Vault not found or malformed.")
        return

    # Reconcile entries in the vault
    summary = reconcile_entries(vault)

    # Output the summary of reconciled entries
    print("Reconciliation Summary:")
    print(summary)

if __name__ == "__main__":
    main()