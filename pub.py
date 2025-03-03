import paho.mqtt.client as mqtt
import time
import json
import random
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def log_result(result: mqtt.MQTTMessageInfo, topic: str):
    # result = client.publish("topic/test", message)  # Publish message to topic
    status = result[0]
    if status == 0:
        print(f"Send `{result}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic due to {status}")

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect("localhost", 1883, 60)  # Connect to the MQTT broker (adjust the IP if needed)
    client.loop_start()  # Start the loop in the background

    try: 
        while True:
            temperature = random.uniform(18, 30)  # Aloe Vera thrives between 18°C and 30°C
            humidity = random.uniform(40, 60)     # Ideal humidity for Aloe Vera
            now = int(time.time())
            data = {
                "time": now,
                "temperature": temperature,
                "humidity": humidity
            }

            result = client.publish("smartplanter/data", json.dumps(data))
            log_result(result, "smartplanter/data")
            time.sleep(5)

    except KeyboardInterrupt:
        print("Stopping publisher...")
        client.loop_stop()
        client.disconnect()

