from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# ---------- Database Connection ----------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sensor_db"
    )

# ---------- CREATE ----------
@app.route("/moisture", methods=["POST"])
def add_record():
    data = request.get_json()

    con = get_db_connection()
    cur = con.cursor()

    query = """
        INSERT INTO soil_moisture (sensor_id, moisture_level, date_time)
        VALUES (%s, %s, %s)
    """
    cur.execute(query, (
        data["sensor_id"],
        data["moisture_level"],
        datetime.now()
    ))

    con.commit()
    cur.close()
    con.close()

    return jsonify({"message": "Record inserted successfully"}), 201

# ---------- READ ALL ----------
@app.route("/moisture", methods=["GET"])
def get_all_records():
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute("SELECT * FROM soil_moisture")
    rows = cur.fetchall()

    cur.close()
    con.close()

    return jsonify(rows)

# ---------- READ BY SENSOR ID ----------
@app.ro
