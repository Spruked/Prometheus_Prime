
# Prometheus Prime Core System - Unified File

import os
import sqlite3
import base64
import uuid
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from flask import Flask, request, jsonify

DB_PATH = "legacy_vault.db"
KEY_VAULT_NAME = "your-keyvault-name"
SECRET_NAME = "encryption-key"
vault_url = f"https://{KEY_VAULT_NAME}.vault.azure.net"
credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url, credential)

app = Flask(__name__)

# Scaffold core structure
DIRECTORIES = [
    "System_Core/FIRE_Engine",
    "System_Core/EchoStack",
    "Companions/Prometheus",
    "Companions/CATO",
    "Companions/Archimedes",
    "Vault/Genesis_Ledger",
    "Vault/Memory_Cache",
    "Interface/Rituals",
    "Interface/UX_Screens",
    "Logs/Companion_Behavior"
]

def create_structure():
    for d in DIRECTORIES:
        os.makedirs(os.path.join("PrometheusPrime", d), exist_ok=True)

# Vault logic and message utilities here...
# (truncated for brevity - full file was generated before)

# Flask routes and startup
@app.route('/vaults/<vault_id>/messages', methods=['GET'])
def get_messages(vault_id):
    conn = sqlite3.connect(DB_PATH)
    messages = conn.execute(
        "SELECT * FROM vault_messages WHERE vault_id = ? ORDER BY created_at ASC", 
        (vault_id,)
    ).fetchall()
    conn.close()
    return jsonify([dict(m) for m in messages])

@app.route('/vaults/<vault_id>/messages', methods=['POST'])
def add_message(vault_id):
    data = request.get_json()
    message_id = str(uuid.uuid4())
    message_text = data.get("content")
    media_url = data.get("media_url", "")
    if not message_text:
        return jsonify({'status': 'error', 'message': 'Message content required'}), 400
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO vault_messages (message_id, vault_id, message_text, media_url) VALUES (?, ?, ?, ?)",
        (message_id, vault_id, message_text, media_url)
    )
    conn.commit()
    conn.close()
    return jsonify({'status': 'success', 'vault_id': vault_id, 'message_id': message_id, 'message_text': message_text}), 201

if __name__ == "__main__":
    print("And now, it begins.")
    create_structure()
    app.run(debug=True)
