from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "smart_home.db"

# ---------- Database Connection ----------
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS smart_home_status (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            light_status TEXT,
            fan_status TEXT,
            temperature REAL,
            timestamp DATETIME
        )
    """)
    conn.commit()
    conn.close()

init_db()
