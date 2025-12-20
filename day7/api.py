import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="smart_home"

from flask import Blueprint,jsonify
from db_connection.py import get_db_connection

delete_api = Blueprint("delete_api", __name__)

@delete_api.route("/sensor/<int:id>", methods=["DELETE"])
def delete_sensor(id):
    con = get_db_connection()
    cur = con.cursor()

    cur.execute("DELETE FROM sensor_readings WHERE id=%s", (id,))
    con.commit()

    cur.close()
    con.close()

    return jsonify({"message": "Sensor reading deleted"})
    )