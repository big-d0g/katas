test:
	python3 -m unittest

lint:
	ruff format
	ruff check --select I --fix
