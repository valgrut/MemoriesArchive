init:
	pip install -r requirements.txt

test:
	py.test tests

run:
	python3 run_app.py

.PHONY: init test
