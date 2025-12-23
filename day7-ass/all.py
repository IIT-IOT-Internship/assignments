
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

# ---------- Create Table ----------
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

# ---------- Update Sensor Data ----------
@app.route("/update", methods=["POST"])
def update_status():
    data = request.json

    light_status = data.get("light_status")
    fan_status = data.get("fan_status")
    temperature = data.get("temperature")

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO smart_home_status
        (light_status, fan_status, temperature, timestamp)
        VALUES (?, ?, ?, ?)
    """, (light_status, fan_status, temperature, datetime.now()))

    conn.commit()
    conn.close()

    return jsonify({"message": "Status updated successfully"})

# ---------- Get Current Status ----------
@app.route("/status", methods=["GET"])
def get_status():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT light_status, fan_status, temperature
        FROM smart_home_status
        ORDER BY timestamp DESC
        LIMIT 1
    """)
    row = cur.fetchone()
    conn.close()

    if row is None:
        return jsonify({"message": "No data available"})

    return jsonify({
        "Light": row["light_status"],
        "Fan": row["fan_status"],
        "Temperature": row["temperature"]
    })

# ---------- Run Server ----------
if __name__ == "__main__":
    app.run(debug=True)
