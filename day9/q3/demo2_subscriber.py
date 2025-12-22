import paho.mqtt.client as mqtt
import mysql.connector
import json
from datetime import datetime

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="smart_home"
    )

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    appliance = data["appliance"]
    status = data["status"]

    con = get_db()
    cur = con.cursor()

    cur.execute(
        "INSERT INTO appliance_status (appliance_name, status, timestamp) VALUES (%s,%s,%s)",
        (appliance, status, datetime.now())
    )

    con.commit()
    cur.close()
    con.close()

    print(f"{appliance} turned {status}")

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("home/control")
client.on_message = on_message

print("Waiting for control commands...")
client.loop_forever()
