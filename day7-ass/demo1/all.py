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

# ---------- READ (ALL) ----------
@app.route("/sensor", methods=["GET"])
def get_all_sensors():
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute("SELECT * FROM sensor_readings")
    rows = cur.fetchall()

    cur.close()
    con.close()

    return jsonify(rows)

# ---------- READ (BY ID) ----------
@app.route("/sensor/<int:id>", methods=["GET"])
def get_sensor(id):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    cur.execute("SELECT * FROM sensor_readings WHERE id=%s", (id,))
    row = cur.fetchone()

    cur.close()
    con.close()

    return jsonify(row)

# ---------- UPDATE ----------
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

# ---------- DELETE ----------
@app.route("/sensor/<int:id>", methods=["DELETE"])
def delete_sensor(id):
    con = get_db_connection()
    cur = con.cursor()

    cur.execute("DELETE FROM sensor_readings WHERE id=%s", (id,))
    con.commit()

    cur.close()
    con.close()

    return jsonify({"message": "Sensor reading deleted successfully"})

# ---------- BELOW THRESHOLD ----------
@app.route("/sensor/below/<float:value>", methods=["GET"])
def below_threshold(value):
    con = get_db_connection()
    cur = con.cursor(dictionary=True)

    query = """
        SELECT * FROM sensor_readings
        WHERE temperature < %s OR humidity < %s
    """
    cur.execute(query, (value, value))
    rows = cur.fetchall()

    cur.close()
    con.close()

    return jsonify(rows)

# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(debug=True)
