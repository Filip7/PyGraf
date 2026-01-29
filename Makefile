SHELL := /bin/bash

setup-env:
	uv venv

setup-install:
	uv sync

run:
	python pygraf/main.py

build:
	pyinstaller -F -p pygraf -n pygraf pygraf/main.py

clean:
	rm -rf build/ dist/

help:
	@printf "Usage:\nmake setup-env     -> setup the uv virtual environment\nmake setup-install -> install dependencies using uv\nmake run           -> start application\nmake build         -> produce executable\nmake help          -> show this help\n"
