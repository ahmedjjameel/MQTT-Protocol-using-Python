# MQTT Protocol using Python 

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol designed for low-bandwidth, high-latency, or unreliable networks. It's commonly used in IoT (Internet of Things) applications, where devices need to communicate with each other efficiently.
To install the MQTT library on Windows and use it with Python, you can follow these steps:
Installing the MQTT Library on Windows:
1.	Install Python: If you haven't already, download and install Python from the official website: python.org.
2.	Install PIP: PIP is a package manager for Python. It usually comes pre-installed with Python, but if not, you can install it by following the instructions here.
3.	Install paho-mqtt: Paho MQTT is a Python implementation of the MQTT protocol. You can install it using PIP by running the following command in your command prompt or terminal:
   
pip install paho-mqtt

# Using MQTT with Python:
Once you have installed the paho-mqtt library, you can start using MQTT in your Python scripts. Here's a simple example of how to publish and subscribe to MQTT messages:

## Example 1: Publishing_Messages.py
import paho.mqtt.client as mqtt
import time

### Define callback function for MQTT on_connect event
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Failed to connect, return code %d\n", rc)

### Create an MQTT client instance
client = mqtt.Client()

### Set callback function for MQTT on_connect event
client.on_connect = on_connect

### Connect to the MQTT broker
client.connect("test.mosquitto.org", 1883, 60)

### Start the MQTT client loop to handle incoming and outgoing messages
client.loop_start()

### Publish messages every 5 seconds
while True:
    client.publish("topic/test", "Hello, MQTT!")
    print("Message published")
    time.sleep(5)



## Example 2: Subscribing-to-Messages.py
import paho.mqtt.client as mqtt

### Define callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("topic/test")
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    print("Received message: ", str(msg.payload.decode("utf-8")))

### Create an MQTT client instance
client = mqtt.Client()

### Set callback functions
client.on_connect = on_connect
client.on_message = on_message

### Connect to the MQTT broker
client.connect("test.mosquitto.org", 1883, 60)

### Start the MQTT client loop to handle incoming messages
client.loop_forever()


## Running the Scripts:
1.	Save the Publishing_Messages.py and Subscribing-to-Messages.py scripts in separate files.
2.	Open two command prompt or terminal windows.
3.	In one window, run the Publisher script:
python Publishing_Messages.py
4.	In the other window, run the Subscriber script:
python Subscribing-to-Messages.py
You should see the Subscriber window displaying the message "Hello, MQTT!" received from the Publisher.
This is just a basic example to get you started with MQTT in Python. You can explore more features and functionalities of the MQTT protocol and the paho-mqtt library as you delve deeper into your project requirements.



![video](https://github.com/ahmedjjameel/MQTT-Protocol-using-Python/assets/81799459/14cacd49-487c-4869-bd02-a8463afc1af0)
