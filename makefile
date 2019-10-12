MAKEFLAGS+="j 2"

run: celery flask

flask:
	python3 app.py

celery:
	celery -A app worker --loglevel=info

run_user_script:
	python3 user_script.py

install:
	curl http://user.it.uu.se/~meos6185/data.tar.gz | tar xz

clean:
	rm -rf data/
