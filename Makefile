SHELL := /bin/bash

setup-env:
	pipenv shell

setup-install:
	pipenv install

run:
	python pygraf/main.py

build:
	pyinstaller -F -p pygraf -n pygraf pygraf/main.py

clean:
	rm -rf build/ dist/

help:
	@printf "Usage:\nmake setup-env     -> setup the pipenv shell\nmake setup-install -> install dependencies\nmake run           -> start application\nmake build         -> produce executable\nmake help          -> show this help\n"
