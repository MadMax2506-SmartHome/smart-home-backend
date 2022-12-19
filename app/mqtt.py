from paho.mqtt import client as mqtt_client


class Mqtt:
    def __init__(self, broker, port, client_id):
        self._client = None
        self._connect_mqtt(broker, port, client_id)

    def publish(self, topic, msg):
        return self._client.publish(topic, msg)

    def subscribe(self, topic, on_message):
        self._client.subscribe(topic)
        self._client.on_message = on_message

    def _connect_mqtt(self, broker, port, client_id):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        self._client = mqtt_client.Client(client_id)
        self._client.on_connect = on_connect
        self._client.connect(broker, port)
        self._client.loop_start()
