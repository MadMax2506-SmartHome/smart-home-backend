import json


def string_to_json(string):
    return json.loads(string)


def update_received_devices(old_values: list, new_value):
    new_values = [new_value]

    for elem in old_values:
        if new_value["info"]["deviceId"] == elem["info"]["deviceId"]:
            continue
        else:
            new_values.append(elem)

    return new_values
