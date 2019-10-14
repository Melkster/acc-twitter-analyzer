MAKEFLAGS+="j 2"

run_server: celery flask

flask:
	python3 app.py

celery:
	celery -A app worker --loglevel=info

install:
	curl http://user.it.uu.se/~meos6185/data.tar.gz | tar xz

clean:
	rm -rf data/
