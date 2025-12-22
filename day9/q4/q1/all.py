import paho.mqtt.client as mqtt
import mysql.connector
import json
import time
import random
from datetime import datetime

# ---------- THRESHOLDS (CHANGE AS PER YOUR CHOICE) ----------
TEMP_THRESHOLD = 35      # Fan ON if temp > 35
LDR_THRESHOLD = 300      # Light ON if intensity < 300

# ---------- DATABASE CONNECTION ----------
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="smart_home"
    )

# ---------- MQTT CALLBACK ----------
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    con = get_db()
    cur = con.cursor()

    if msg.topic == "sensor/ldr":
        value = data["intensity"]
        sensor = "LDR"

        status = "LIGHT ON" if value < LDR_THRESHOLD else "LIGHT OFF"

    elif msg.topic == "sensor/lm35":
        value = data["temperature"]
        sensor = "LM35"

        status = "FAN ON" if value > TEMP_THRESHOLD else "FAN OFF"

    # Insert into database
    cur.execute(
        "INSERT INTO sensor_data (sensor_type, value, timestamp) VALUES (%s,%s,%s)",
        (sensor, value, datetime.now())
    )

    con.commit()
    cur.close()
    con.close()

    # Custom Output
    print(f"{sensor} | Value: {value} | Status: {status}")

# ---------- MQTT SETUP ----------
client = mqtt.Client(client_id="smart_home_all")
client.connect("localhost", 1883, 60)

client.subscribe("sensor/ldr")
client.subscribe("sensor/lm35")
client.on_message = on_message

client.loop_start()

print("Smart Home System Running...\n")

# ---------- PUBLISH SENSOR DATA ----------
while True:
    ldr_data = {"intensity": random.randint(0, 1023)}
    lm35_data = {"temperature": round(random.uniform(20, 45), 2)}

    client.publish("sensor/ldr", json.dumps(ldr_data))
    client.publish("sensor/lm35", json.dumps(lm35_data))

    time.sleep(5)
