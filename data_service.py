from fastapi import FastAPI
from typing import List
import json

import paho.mqtt.client as mqtt

app = FastAPI()


mqtt_broker = "localhost"
mqtt_topic = "smartplanter/data"
data_storage: List[dict] = []

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    data = msg.payload.decode()
    if msg.topic == "smartplanter/data":
        data = json.loads(msg.payload.decode())
        print(f"Received data: {data}")
        data_storage.append(data)

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(mqtt_broker, 1883, 60)
mqtt_client.loop_start()

@app.get("/data")
def get_data():
    data_str = json.dumps(data_storage)
    print(f"Data sent: {data_str}")
    return data_str