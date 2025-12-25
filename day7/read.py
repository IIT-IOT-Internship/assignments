from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# -------------------------------
# Database Connection
# -------------------------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="sensor_db"
    )
@app.route("/sensor", methods=["GET"])
def get_all_sensors():
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute("SELECT * FROM sensor_readings")
    rows = cur.fetchall()

    cur.close()
    con.close()

    return jsonify(rows)