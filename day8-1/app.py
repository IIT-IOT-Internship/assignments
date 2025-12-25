from flask import Flask, request, jsonify
from database import get_db_connection, create_table

app = Flask(__name__)
create_table()

# ---------------- UPDATE SENSOR DATA ----------------
@app.route("/update", methods=["POST"])
def update_sensor():
    data = request.json

    light_status = data.get("light_status")
    fan_status = data.get("fan_status")
    temperature = data.get("temperature")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO sensor_data (light_status, fan_status, temperature) VALUES (?, ?, ?)",
        (light_status, fan_status, temperature)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Sensor data updated successfully"}), 201


# ---------------- STATUS API ----------------
@app.route("/status", methods=["GET"])
def get_status():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT light_status, fan_status, temperature FROM sensor_data ORDER BY id DESC LIMIT 1"
    )
    row = cur.fetchone()
    conn.close()

    if row:
        return jsonify({
            "light_status": row[0],
            "fan_status": row[1],
            "temperature": row[2]
        })
    else:
        return jsonify({"message": "No data available"}), 404


if __name__ == "__main__":
    app.run(debug=True)
