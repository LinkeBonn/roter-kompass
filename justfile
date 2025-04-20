set dotenv-load := true

export PROJECT_ROOT := justfile_directory()
export UID := if os() == 'linux' { `id -u ` } else { '0' }
export GID := if os() == 'linux' { `id -g ` } else { '0' }
export ENV_FILE := if path_exists('.env.local') == 'true' { '.env.local' } else { '.env' }

# Format: <dockerFile>-COMPOSE-RUN-<dockerService>
WEB-APP-COMPOSE := 'docker compose -p ' + env_var('NAME') + ' -f config/docker-compose/web-app.yml --env-file ' + ENV_FILE
WEB-APP-COMPOSE-RUN := WEB-APP-COMPOSE + ' run --rm'
WEB-APP-NODE-RUN := WEB-APP-COMPOSE-RUN + ' --no-deps web-app'
WEB-APP-PYTHON-RUN := WEB-APP-COMPOSE-RUN + ' --no-deps backend'

help:
	@just --list

npm *args='-h':
	{{WEB-APP-NODE-RUN}} npm {{args}}

npx *args='-h':
	{{WEB-APP-NODE-RUN}} npx {{args}}

enter:
	{{WEB-APP-NODE-RUN}} bash

pip *args='-h':
    {{WEB-APP-PYTHON-RUN}} .venv/bin/pip3.11 {{args}}
    {{WEB-APP-PYTHON-RUN}} .venv/bin/pip3.11 freeze

flask *args='-h':
    {{WEB-APP-PYTHON-RUN}} .venv/bin/python3.11 -m flask {{args}}

db-migrate *args='-h':
    {{WEB-APP-PYTHON-RUN}} .venv/bin/python3.11 -m flask db migrate -m "{{args}}"
    {{WEB-APP-PYTHON-RUN}} .venv/bin/python3.11 -m flask db upgrade

install:
	@just build-docker-images
	{{WEB-APP-NODE-RUN}} npm install --inline-builds
	@echo "\n Web App Install finished 🎉"
	{{WEB-APP-PYTHON-RUN}} python3 -m venv .venv
	{{WEB-APP-PYTHON-RUN}} .venv/bin/pip3.11 install -r requirements.txt
	@echo "\n Backend Install finished 🎉"

build:
    {{WEB-APP-NODE-RUN}} npm build

typecheck:
    {{WEB-APP-NODE-RUN}} npm typecheck

start: stop
	{{WEB-APP-COMPOSE}} up -d
	@just status

stop:
	{{WEB-APP-COMPOSE}} down

@exec *args:
	{{WEB-APP-COMPOSE}} exec web-app {{args}}

compose *args:
	{{WEB-APP-COMPOSE}} {{args}}

status:
	@just compose ps

# Pull latest upstream images and build local Docker images
build-docker-images:
	{{WEB-APP-COMPOSE}} build --pull --parallel

build-web-app: (npm "build")

pre-commit: format-fix lint-fix

################################################
# TESTS
################################################

format-fix:
	just npm format:fix

lint-fix:
	just npm lint:fix

format-check:
	just npm format

lint-check:
	just npm lint