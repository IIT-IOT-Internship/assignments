import paho.mqtt.client as mqtt
import mysql.connector
import json
from datetime import datetime

# ---------- Database Connection ----------
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="smart_home"
    )

# ---------- On Message ----------
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    con = get_db()
    cur = con.cursor()

    if msg.topic == "sensor/ldr":
        value = data["intensity"]
        sensor = "LDR"

    elif msg.topic == "sensor/lm35":
        value = data["temperature"]
        sensor = "LM35"

    cur.execute(
        "INSERT INTO sensor_data (sensor_type, value, timestamp) VALUES (%s,%s,%s)",
        (sensor, value, datetime.now())
    )

    con.commit()
    cur.close()
    con.close()

    print(f"Stored {sensor} Data:", value)

# ---------- MQTT Setup ----------
client = mqtt.Client(client_id="smart_home_subscriber")
client.connect("localhost", 1883, 60)

client.subscribe("sensor/ldr")
client.subscribe("sensor/lm35")

client.on_message = on_message

print("Smart Home Subscriber Running...")
client.loop_forever()
