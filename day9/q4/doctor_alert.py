import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("Doctor Alert:", msg.payload.decode())

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("health/alert")
client.on_message = on_message

client.loop_forever()
