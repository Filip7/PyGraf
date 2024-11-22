SHELL := /bin/bash

setup-env:
	source venv/bin/activate

setup-install:
	pipenv install

run:
	python pygraf/main.py

build:
	pyinstaller -F pygraf/main.py -p pygraf
