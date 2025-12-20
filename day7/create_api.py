import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="smart_home"
    )

from flask import Blueprint, request, jsonify
from db_config import get_db_connection
from datetime import datetime

create_api = Blueprint("create_api", __name__)

@create_api.route("/sensor", methods=["POST"])
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

    return jsonify({"message": "Sensor reading added"})
