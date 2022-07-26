install:
	poetry install
brain-games:
	poetry run brain-games
even-games:
	poetry run even-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
make lint:
	poetry run flake8 brain_games
