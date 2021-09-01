clean: install
	rm -rf build dist .eggs *.egg-info

tests: requirements
	echo Running tests ...
	python -m unittest --verbose

requirements:
	echo Installing requirements ...
	pip install -r requirements.txt

install: tests
	python setup.py install