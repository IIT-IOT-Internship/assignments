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

@app.route("/sensor", methods=["POST"])
def add_sensor():
    data = request.json
    con = get_db_connection()
    cur = con.cursor()

    query = """
    INSERT INTO sensor_readings (temperature, humidity, timestamp)
    VALUES (%s, %s, %s)
    """
    cur.execute(query, (
        data["temperature"],
        data["humidity"],
        datetime.now()
    ))

    con.commit()
    cur.close()
    con.close()

    return jsonify({"message": "Sensor reading added successfully"})