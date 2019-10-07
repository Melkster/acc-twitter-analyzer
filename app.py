#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello_world', methods=['GET'])
def hello_world():
    return "Hello World!\n"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
