from fastapi import APIRouter, HTTPException
from cali.vault.vaultkeeper import load_memory_vault, save_memory_vault
from cali.vault.reconciliation import reconcile_vault

router = APIRouter()

@router.post("/vault/{vault_id}/reconcile")
def reconcile_vault_route(vault_id: str):
    vault = load_memory_vault(vault_id)
    if not vault:
        raise HTTPException(status_code=404, detail="Vault not found.")
    
    result = reconcile_vault(vault_id, vault)
    return result