import paho.mqtt.client as mqtt
import time

# Define callback function for MQTT on_connect event
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Failed to connect, return code %d\n", rc)

# Create an MQTT client instance
client = mqtt.Client()

# Set callback function for MQTT on_connect event
client.on_connect = on_connect

# Connect to the MQTT broker
client.connect("test.mosquitto.org", 1883, 60)

# Start the MQTT client loop to handle incoming and outgoing messages
client.loop_start()

# Publish messages every 5 seconds
while True:
    client.publish("topic/test", "Hello, MQTT!")
    print("Message published")
    time.sleep(5)
