from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# ---------- Database Connection ----------
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="sensor_db"
    )
@app.route("/sensor/<int:id>", methods=["PUT"])
def update_sensor(id):
    data = request.json
    con = get_db_connection()
    cur = con.cursor()

    query = """
        UPDATE sensor_readings
        SET temperature=%s, humidity=%s
        WHERE id=%s
    """
    cur.execute(query, (
        data["temperature"],
        data["humidity"],
        id
    ))

    con.commit()
    cur.close()
    con.close()

    return jsonify({"message": "Sensor reading updated successfully"})