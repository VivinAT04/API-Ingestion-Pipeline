import json
from pathlib import Path


DATA_FILE = Path("data/processed_data.json")


def store_record(record: dict):
    DATA_FILE.parent.mkdir(exist_ok=True)

    data = []

    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

    data.append(record)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)