import json
import os

test_data_path = os.path.join(os.path.dirname(__file__), "../../test_data.json")


def load_test_cases(test_name: str):
    with open(test_data_path, "r") as f:
        data = json.load(f)
    return data[test_name]
