from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "smart_home.db"

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
