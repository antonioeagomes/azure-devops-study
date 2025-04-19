hello:
	echo "this is my first make command"

install:
	@pip install --upgrade pip
	@pip install -r requirements.txt

lint:
	@echo "Running linters..."
	@pylint --disable=R,C,E1120,W0613 hello.py

test_hello:
	@echo "Running tests..."
	@pytest -vv test_hello.py