MAKEFLAGS+="j 2"

run: celery python

python:
	python3 app.py

celery:
	celery -A app.celery worker --loglevel=info

install:
	curl http://user.it.uu.se/~meos6185/data.tar.gz | tar xz

clean:
	rm -rf data/
