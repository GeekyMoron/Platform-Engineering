import datetime
import socket

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/v1/hello')
def hello_world():
    return jsonify({'message': 'Hello World'}), 200


@app.route('/v1/health')
def health():
    return jsonify({'message': 'NG ki maki chut', 'time': datetime.datetime.now(), 'hostname': socket.gethostname()}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)