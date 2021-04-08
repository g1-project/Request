SHELL := /bin/bash # Use bash syntax
CURRENT_DIR := $(shell pwd)
RUNNING_NETWORK := $(shell docker network ls -f name=lendit | grep lendit )


build:
	chmod +x entrypoint.sh
	sudo docker-compose -f docker-compose.dev.yml build

run:
	@if [[ -d "${RUNNING_NETWORK}" ]]; then \
		sudo docker-compose -f docker-compose.dev.yml up; \
	else \
		sudo docker network create lendit_gateway; \
		sudo docker-compose -f docker-compose.dev.yml up; \
	fi
	

run-silent:
	@if [[ -d "${RUNNING_NETWORK}" ]]; then \
		sudo docker-compose -f docker-compose.dev.yml up -d; \
	else \
		sudo docker network create lendit_gateway; \
		sudo docker-compose -f docker-compose.dev.yml up -d; \
	fi

run-build:
	@if [[ -d "${RUNNING_NETWORK}" ]]; then \
		chmod +x entrypoint.sh; \
		sudo docker-compose -f docker-compose.dev.yml up --build; \
	else \
		chmod +x entrypoint.sh; \
		sudo docker network create lendit_gateway; \
		sudo docker-compose -f docker-compose.dev.yml up --build; \
	fi

test:
	sudo docker-compose -f docker-compose.dev.yml run request python manage.py test

lint:
	sudo docker-compose -f docker-compose.dev.yml run request black .

check-db:
	sudo docker-compose -f docker-compose.dev.yml exec db psql -U postgres

down:
	sudo docker-compose -f docker-compose.dev.yml down

recreate-db:
	sudo docker-compose -f docker-compose.dev.yml run request python manage.py recreate-db

cov-html:
	sudo docker-compose -f docker-compose.dev.yml run request python manage.py cov;
	google-chrome  $(CURRENT_DIR)/htmlcov/index.html;