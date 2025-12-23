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
    
    
@app.route("/sensor/<int:id>", methods=["DELETE"])
def delete_sensor(id):
    con = get_db_connection()
    cur = con.cursor()

    cur.execute("DELETE FROM sensor_readings WHERE id=%s", (id,))
    con.commit()

    cur.close()
    con.close()

    return jsonify({"message": "Sensor reading deleted successfully"})