import paho.mqtt.client as mqtt

broker = "157.173.101.159"
port = 1883
topic = "/student_group/light_control"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(topic)
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    if payload == "ON":
        print("💡 Light is TURNED ON")
    elif payload == "OFF":
        print("💡 Light is TURNED OFF")
    else:
        print(f"Unknown command: {payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_forever()
