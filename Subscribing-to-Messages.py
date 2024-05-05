import paho.mqtt.client as mqtt

# Define callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("topic/test")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    print("Received message: ", str(msg.payload.decode("utf-8")))

# Create an MQTT client instance
client = mqtt.Client()

# Set callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect("test.mosquitto.org", 1883, 60)

# Start the MQTT client loop to handle incoming messages
client.loop_forever()
