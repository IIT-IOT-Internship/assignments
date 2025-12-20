import sqlite3

DB_NAME = "smarthome.db"

def get_db_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            light_status TEXT,
            fan_status TEXT,
            temperature REAL
        )
    """)
    conn.commit()
    conn.close()
