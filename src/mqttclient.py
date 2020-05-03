import paho.mqtt.client as mqtt

MQTT_BROKER_HOST = 'localhost'
MQTT_BROKER_PORT = '1833'
MQTT_KEEP_ALIVE_INTERVAL = '60'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("building/*")

def on_message(client, userdata, message):
    print("message received ", message.payload.decode())


client = mqtt.Client()
client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_KEEP_ALIVE_INTERVAL)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
