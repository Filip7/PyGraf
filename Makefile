SHELL := /bin/bash

setup-env:
	source venv/bin/activate

setup-install:
	pipenv install

run:
	python pygraf/main.py

build:
	pyinstaller -F -p pygraf -n pygraf pygraf/main.py

clean:
	rm -rf build/ dist/
