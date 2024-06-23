lint:
	poetry run flake8 .

test-coverage:
	poetry run pytest --cov=gendiff --cov-report=term-missing --cov-report=xml
