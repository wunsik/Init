SHELL := /bin/bash

bootstrap:
	mkdir -p _workspace/{drafts,reviews,generated,exports,logs,temp}

install:
	python3 -m pip install -r services/api/requirements.txt
	cd apps/frontend && npm install

up:
	docker compose up --build

test:
	cd services/api && python3 -m pytest -q

format:
	@echo "Add formatter hooks as needed"

precommit:
	bash scripts/pre-commit.sh
