import paho.mqtt.client as mqtt
import json
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

command = {
    "appliance": "Light",
    "status": "ON"
}

client.publish("home/control", json.dumps(command))
print("Command sent:", command)

time.sleep(1)
client.disconnect()
