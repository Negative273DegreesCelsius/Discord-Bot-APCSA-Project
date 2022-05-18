import json

def get_json(file):
    with open(file, "r") as f:
        data = json.load(f)
        return data