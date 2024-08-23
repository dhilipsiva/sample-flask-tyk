import time
import json
import random
import string
from flask import Flask


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_large_json(num_entries, key_length, value_length):
    data = {}
    for _ in range(num_entries):
        key = generate_random_string(key_length)
        value = generate_random_string(value_length)
        data[key] = value
    return data

app = Flask(__name__)

@app.route('/')
def delayed_response():
    num_entries = 300000
    key_length = 10
    value_length = 100
    json_data = generate_large_json(num_entries, key_length, value_length)
    json_string = json.dumps(json_data, indent=2)
    # time.sleep(5)
    return json_string

if __name__ == '__main__':
    app.run(debug=True)

