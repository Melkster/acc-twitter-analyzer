run:
	python3 app.py

install:
	curl http://user.it.uu.se/~meos6185/data.tar.gz | tar xz

clean:
	rm -rf data/
