import paho.mqtt.client as mqtt
import time
import random
import json

BROKER = "localhost"
PORT = 8

client = mqtt.Client()
client.connect(BROKER, PORT)

while True:
    temperature = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(40, 70), 2)

    temp_data = {
        "value": temperature,
        "unit": "C"
    }

    hum_data = {
        "value": humidity,
        "unit": "%"
    }

    client.publish("home/livingroom/temperature", json.dumps(temp_data))
    client.publish("home/livingroom/humidity", json.dumps(hum_data))

    print("Published:", temp_data, hum_data)
    time.sleep(5)
