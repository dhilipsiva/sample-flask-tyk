from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def delayed_response():
    time.sleep(120)
    return "delayed respose"

if __name__ == '__main__':
    app.run(debug=True)

