from flask import Blueprint, request, jsonify
from db_config import get_db_connection

update_api = Blueprint("update_api", __name__)

@update_api.route("/sensor/<int:id>", methods=["PUT"])
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

    return jsonify({"message": "Sensor reading updated"})
