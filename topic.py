from paho.mqtt.client import MQTTMessage

from mqtt import Mqtt


class Topic:
    def __init__(self, client: Mqtt, topic_prefix, update_received_messages, parse_message=None):
        self._subscribed_messages = []

        self._client = client
        self._topic_prefix = topic_prefix
        self._update_received_messages = update_received_messages
        self._parse_message = parse_message

    def get_subscribed_messages(self):
        return self._subscribed_messages

    def publish(self, msg):
        topic = f"conf/{self._topic_prefix}"
        result = self._client.publish(topic, msg)

        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

    def subscribe(self):
        def on_message(client, userdata, msg: MQTTMessage):
            payload = msg.payload
            parsed_payload = (payload if self._parse_message is None else self._parse_message(payload))
            print(parsed_payload)
            self._subscribed_messages = self._update_received_messages(self._subscribed_messages, parsed_payload)

        topic = f"status/{self._topic_prefix}"
        self._client.subscribe(topic, on_message)
        print(f"Subscribe '{topic}'")
