# justfile, see https://github.com/casey/just for more information
set dotenv-load := true

export PROJECT_ROOT := justfile_directory()
export UID := if os() == 'linux' { `id -u ` } else { '0' }
export GID := if os() == 'linux' { `id -g ` } else { '0' }
export ENV_FILE := if path_exists('.env.local') == 'true' { '.env.local' } else { '.env' }

# Format: <dockerFile>-COMPOSE-RUN-<dockerService>
WEB-APP-COMPOSE := 'docker compose -p ' + env_var('NAME') + ' -f config/docker-compose/web-app.yml --env-file ' + ENV_FILE
WEB-APP-COMPOSE-RUN := WEB-APP-COMPOSE + ' run --rm'
WEB-APP-NODE-RUN := WEB-APP-COMPOSE-RUN + ' --no-deps web-app'

help:
	@just --list

npm *args='-h':
	{{WEB-APP-NODE-RUN}} npm {{args}}

npx *args='-h':
	{{WEB-APP-NODE-RUN}} npx {{args}}

enter:
	{{WEB-APP-NODE-RUN}} bash

install:
	@just build-docker-images
	{{WEB-APP-NODE-RUN}} npm install --inline-builds
	@echo "\n Install finished 🎉"

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