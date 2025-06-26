-- Main Legacy Vault Table
CREATE TABLE legacy_vault (
    vault_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    trigger_keywords TEXT,
    delivery_mode TEXT,
    unlock_condition TEXT,
    is_active INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Vault Messages Table
CREATE TABLE vault_messages (
    message_id TEXT PRIMARY KEY,
    vault_id TEXT,
    message_text TEXT,
    media_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vault_id) REFERENCES legacy_vault (vault_id)
);
