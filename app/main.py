import os

from dotenv import load_dotenv
from fastapi import FastAPI

from app.mqtt import Mqtt
from app.topic import Topic
from app.utils import string_to_json, update_received_devices

load_dotenv()

client = Mqtt(
    broker=os.getenv('BROKER_ADDRESS'),
    port=int(os.getenv('BROKER_PORT')),
    client_id=os.getenv('BROKER_CLIENT_ID')
)
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
    return devices_topic.get_subscribed_messages()

