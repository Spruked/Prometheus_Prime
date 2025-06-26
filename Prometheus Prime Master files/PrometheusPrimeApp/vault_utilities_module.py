
import sqlite3
import os
import base64
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

DB_PATH = "legacy_vault.db"
KEY_VAULT_NAME = "your-keyvault-name"
SECRET_NAME = "encryption-key"
vault_url = f"https://{KEY_VAULT_NAME}.vault.azure.net"
credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url, credential)

def delete_vault_record(vault_id: str) -> str:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT vault_id FROM legacy_vault WHERE vault_id = ?", (vault_id,))
    if not cursor.fetchone():
        conn.close()
        return f"Error: No record found for Vault ID {vault_id}"
    cursor.execute("DELETE FROM legacy_vault WHERE vault_id = ?", (vault_id,))
    conn.commit()
    conn.close()
    return f"Vault record {vault_id} permanently deleted."

def decrypt_data(encrypted_data: str, key: str) -> str:
    encrypted_bytes = base64.b64decode(encrypted_data)
    cipher = AES.new(key.encode("utf-8"), AES.MODE_ECB)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
    return decrypted_bytes.decode("utf-8")

def export_vault_record(vault_id: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT vault_id, title, description FROM legacy_vault WHERE vault_id = ?", (vault_id,))
    record = cursor.fetchone()
    conn.close()
    if not record:
        return f"Error: No record found for Vault ID {vault_id}"
    encryption_key = secret_client.get_secret(SECRET_NAME).value
    decrypted_description = decrypt_data(record[2], encryption_key)
    os.makedirs("exports", exist_ok=True)
    filename = f"exports/{record[1].replace(' ', '_')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Vault ID: {record[0]}\n")
        file.write(f"Title: {record[1]}\n")
        file.write(f"Description:\n{decrypted_description}\n")
    return f"Vault record {vault_id} exported successfully as {filename}"

def fetch_active_vault_records():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(legacy_vault)")
    columns = [col[1] for col in cursor.fetchall()]
    if "deleted" in columns:
        cursor.execute("SELECT vault_id, title, created_at FROM legacy_vault WHERE deleted IS NULL OR deleted = 0 ORDER BY created_at DESC")
    else:
        cursor.execute("SELECT vault_id, title, created_at FROM legacy_vault ORDER BY created_at DESC")
    records = cursor.fetchall()
    conn.close()
    return [{"vault_id": r[0], "title": r[1], "created_at": r[2]} for r in records]

def restore_vault_record(vault_id: str) -> str:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT vault_id FROM legacy_vault WHERE vault_id = ? AND deleted = 1", (vault_id,))
    if not cursor.fetchone():
        conn.close()
        return f"Error: No soft-deleted record found for Vault ID {vault_id}"
    cursor.execute("UPDATE legacy_vault SET deleted = 0, deleted_at = NULL WHERE vault_id = ?", (vault_id,))
    conn.commit()
    conn.close()
    return f"Vault record {vault_id} restored successfully."

def lock_vault_record(vault_id: str) -> str:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(legacy_vault)")
    columns = [col[1] for col in cursor.fetchall()]
    if "locked" not in columns:
        cursor.execute("ALTER TABLE legacy_vault ADD COLUMN locked INTEGER DEFAULT 0")
        conn.commit()
    cursor.execute("SELECT vault_id FROM legacy_vault WHERE vault_id = ?", (vault_id,))
    if not cursor.fetchone():
        conn.close()
        return f"Error: No record found for Vault ID {vault_id}"
    cursor.execute("UPDATE legacy_vault SET locked = 1 WHERE vault_id = ?", (vault_id,))
    conn.commit()
    conn.close()
    return f"Vault record {vault_id} locked successfully."

def unlock_vault_record(vault_id: str) -> str:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(legacy_vault)")
    columns = [col[1] for col in cursor.fetchall()]
    if "locked" not in columns:
        cursor.execute("ALTER TABLE legacy_vault ADD COLUMN locked INTEGER DEFAULT 0")
        conn.commit()
    cursor.execute("SELECT vault_id FROM legacy_vault WHERE vault_id = ?", (vault_id,))
    if not cursor.fetchone():
        conn.close()
        return f"Error: No record found for Vault ID {vault_id}"
    cursor.execute("UPDATE legacy_vault SET locked = 0 WHERE vault_id = ?", (vault_id,))
    conn.commit()
    conn.close()
    return f"Vault record {vault_id} unlocked successfully."
