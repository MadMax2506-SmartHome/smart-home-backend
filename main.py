from fastapi import FastAPI

from mqtt import Mqtt
from topic import Topic
from utils import string_to_json, update_received_devices

client = Mqtt(broker="192.168.178.150", port=1883, client_id="smarthome-client")
devices_topic = Topic(
    client,
    topic_prefix="devices",
    parse_message=string_to_json,
    update_received_messages=update_received_devices
)

devices_topic.subscribe()

app = FastAPI()


@app.get("/api/v1/info")
async def info():
    return {"version": 1.0}


@app.put("/api/v1/devices")
async def load_devices():
    devices_topic.publish("list-devices")
    return {}


@app.get("/api/v1/devices")
async def devices():
    return devices_topic.get_subscribed_messages()\

