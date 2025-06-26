from datetime import datetime
import sqlite3

class WhisperingArchive:
    def __init__(self, db_path='codex_archive.db'):
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS echo_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            context TEXT,
            output TEXT
        )''')

    def add_entry(self, context, output):
        self.conn.execute('INSERT INTO echo_log (context, output) VALUES (?, ?)', (context, output))
        self.conn.commit()

    def get_entries(self):
        cursor = self.conn.execute('SELECT context, output FROM echo_log ORDER BY id DESC')
        return cursor.fetchall()

