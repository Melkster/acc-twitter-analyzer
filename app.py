#!flask/bin/python
from flask import Flask
from celery import Celery
import os
import json

PATH_TO_DATA = 'data/'

flask_app = Flask(__name__)
celery_app = Celery('app', backend='amqp://', broker='amqp://')

@flask_app.route('/hello_world', methods=['GET'])
def hello_world():
    result = add.delay(10, 12)
    result.wait()
    return str(result.get(timeout=1)) + '\n'

@celery_app.task()
def add(a, b):
    return a + b

# Counts number of occurences of `word` in all files in `path`. Assumes that
# all files in `path` contain JSON objects, where each line is one JSON object
# or empty line.
def count_words(path, word):
    word_count = 0
    tweet_count = 0
    for filename in os.listdir(path):
        f = open(os.path.join(path, filename), 'r')
        for line in f:
            if line not in ['\n', '\r\n']:
                word_count += json.loads(line)['text'].upper().count(word.upper())
                tweet_count += 1
    return word_count, tweet_count


# print(count_words(PATH_TO_DATA, 'han'))

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=True)
