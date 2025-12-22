import paho.mqtt.client as mqtt
import json
import time
import random

client = mqtt.Client()
import paho.mqtt.client as mqtt

client = mqtt.Client(client_id="siddhi_patil")
client.connect("localhost", 1883, 60)



while True:
    data = {
        "pulse": random.randint(60, 120),
        "spo2": random.randint(90, 100)
    }

    client.publish("health/patient", json.dumps(data))
    print("Published:", data)

    time.sleep(5)
