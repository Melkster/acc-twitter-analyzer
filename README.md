# acc-twitter-analyzer

Twitter analyzer for Lab 3 in the course Applied Cloud Computing. The application scans a database of tweets for words submitted by the user and plots how common each word is.

## Dependencies

**Server ([`app.py`](./app.py)):**

- Python 3
- rabbitmq-server (install using your package manager)
- Celery (install using `pip`)
- Flask (install using `pip`)

**Client ([`user_script.py`](./user_script.py)):**

- Python 3
- numbpy (install using `pip`)
- matplotlib (install using `pip`)

## Usage

To download the twitter data, run `make install`. To set up the server, run `make run_server`. Make sure that the `server_url` in [`user_script.py`](./user_script.py) is set to the server's IP adress.

On the client side, to send a request run `python3 user_script.py *words to query*` (make sure that you've cloned this repo to the client as well).
