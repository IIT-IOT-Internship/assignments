import paho.mqtt.client as mqtt
import time
import random
import json

client = mqtt.Client(client_id="smart_home_publisher")
client.connect("localhost", 1883, 60)

while True:
    ldr_data = {
        "intensity": random.randint(0, 1023)
    }

    lm35_data = {
        "temperature": round(random.uniform(20, 40), 2)
    }

    client.publish("sensor/ldr", json.dumps(ldr_data))
    client.publish("sensor/lm35", json.dumps(lm35_data))

    print("Published:", ldr_data, lm35_data)
    time.sleep(5)
