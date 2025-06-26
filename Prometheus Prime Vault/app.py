from flask import Flask, request, jsonify
import sqlite3
import uuid
from datetime import datetime

app = Flask(__name__)
DB_PATH = 'prometheus_vault.db'

# Connect to the SQLite DB
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# 🧠 GET all vaults
@app.route('/vaults', methods=['GET'])
def get_vaults():
    conn = get_db()
    vaults = conn.execute('SELECT * FROM legacy_vault').fetchall()
    conn.close()
    return jsonify([dict(v) for v in vaults])

# 🛠️ POST a new vault
@app.route('/vaults', methods=['POST'])
def add_vault():
    data = request.json
    vault_id = str(uuid.uuid4())
    conn = get_db()
    conn.execute('''
        INSERT INTO legacy_vault (vault_id, title, description, trigger_keywords, delivery_mode, unlock_condition, is_active, created_at, category)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        vault_id,
        data['title'],
        data['description'],
        ",".join(data['trigger_keywords']),
        data['delivery_mode'],
        data['unlock_condition'],
        int(data.get('is_active', 0)),
        datetime.now(),
        data.get('category', '')
    ))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success', 'vault_id': vault_id}), 201

# 💬 POST a new message to a vault
@app.route('/vaults/<vault_id>/messages', methods=['POST'])
def add_message(vault_id):
    data = request.get_json()
    print(f"🔥 Received POST to /vaults/{vault_id}/messages with data: {data}")

    message_id = str(uuid.uuid4())
    message_text = data.get("content")
    media_url = data.get("media_url", "")

    if not message_text:
        return jsonify({'status': 'error', 'message': 'Message content required'}), 400

    conn = get_db()
    conn.execute('''
        INSERT INTO vault_messages (message_id, vault_id, message_text, media_url)
        VALUES (?, ?, ?, ?)
    ''', (message_id, vault_id, message_text, media_url))
    conn.commit()
    conn.close()

    return jsonify({
        'status': 'success',
        'vault_id': vault_id,
        'message_id': message_id,
        'message_text': message_text
    }), 201

# 📥 GET all messages for a specific vault
@app.route('/vaults/<vault_id>/messages', methods=['GET'])
def get_messages(vault_id):
    conn = get_db()
    messages = conn.execute('''
        SELECT * FROM vault_messages
        WHERE vault_id = ?
        ORDER BY created_at ASC
    ''', (vault_id,)).fetchall()
    conn.close()
    return jsonify([dict(m) for m in messages])
# 📡 Add this new root route to avoid "File Not Found" errors
@app.route('/', methods=['GET'])
def root():
    return jsonify({'status': 'running', 'message': 'Prometheus Vault API is online ✅'}), 200

# 🚀 Start the server
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )

# 🚀 Start the server
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )


