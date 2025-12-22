import paho.mqtt.client as mqtt
import mysql.connector
import json
from datetime import datetime

PULSE_THRESHOLD = 100
SPO2_THRESHOLD = 95

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="healthcare_iot"
    )

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    pulse = data["pulse"]
    spo2 = data["spo2"]

    # Store in database
    con = get_db()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO patient_health (pulse, spo2, timestamp) VALUES (%s,%s,%s)",
        (pulse, spo2, datetime.now())
    )
    con.commit()
    cur.close()
    con.close()

    print("Data Stored:", data)

    # Alert condition
    if pulse > PULSE_THRESHOLD or spo2 < SPO2_THRESHOLD:
        alert = f"ALERT! Pulse={pulse}, SpO2={spo2}"
        client.publish("health/alert", alert)
        print("Alert Sent to Doctor:", alert)

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("health/patient")
client.on_message = on_message

print("Healthcare Monitoring Subscriber Running...")
client.loop_forever()
