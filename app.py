#!flask/bin/python
from flask import Flask, request, abort
from celery import Celery
import os
import json

PATH_TO_DATA = 'data/'

flask_app = Flask(__name__)
celery_app = Celery('app', backend='amqp://', broker='amqp://')


@flask_app.route('/', methods=['GET'])
def count_words_request():
    words = request.args.get('words')
    if words is None:
        abort(400, "Did not receive a query.")
    else:
        words = words.split(",")
        response = {'tweet_count': None}

        for word in words:
            result = count_words.delay(PATH_TO_DATA, word)
            result.wait()
            (word_count, tweet_count) = result.get(timeout=1)
            response[word + "_count"] = word_count
            response['tweet_count'] = tweet_count
        return json.dumps(response)

# Counts number of occurences of `word` in all files in `path`. Assumes that
# all files in `path` contain JSON objects, where each line is one JSON object
# or empty line.
@celery_app.task()
def count_words(path, word):
    word_count = 0
    tweet_count = 0
    for filename in os.listdir(path):
        f = open(os.path.join(path, filename), 'r')
        for line in f:
            if line not in ['\n', '\r\n']:
                tweet = json.loads(line)
                if 'retweeted_status' not in tweet:
                    word_count += tweet['text'].upper().count(word.upper())
                    tweet_count += 1
    return (word_count, tweet_count)


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=True)
