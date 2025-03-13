import paho.mqtt.client as mqtt

# MQTT Broker settings
broker = "157.173.101.159"  # Assuming same broker as web interface
port = 1883                  # Standard MQTT port (not WebSockets)
topic = "/student_group/light_control"

# Callback when connected to MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(topic)
    else:
        print(f"Connection failed with code {rc}")

# Callback when a message is received
def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    if payload == "ON":
        print("💡 Light is TURNED ON")
    elif payload == "OFF":
        print("💡 Light is TURNED OFF")
    else:
        print(f"Unknown command: {payload}")

# Setup MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to broker and start loop
client.connect(broker, port, 60)
client.loop_forever()