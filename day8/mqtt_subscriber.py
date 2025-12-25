# install library/module for mqtt
#   pip install paho-mqtt

# import mqtt module
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"message :{message.payload}")

# creat a client to  subscribe topic
subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# add on_message into our subscriber
subscriber.on_message = on_message

# send connect message to publisher
subscriber.connect("localhost")

# subscribe for topic
subscriber.subscribe("sensor/ldr")

# keep subscriber running continuously
subscriber.loop_forever()
