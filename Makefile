.PHONY: help

help: ## This help dialog.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

LOCAL_COMPOSE_FILE ?= ./docker/docker-compose.yml

# ----------------------------------------------------------------------------------------------------------------------
#                                           LOCAL
# ----------------------------------------------------------------------------------------------------------------------
build:  ## Build docker-compose
	docker-compose -f ${LOCAL_COMPOSE_FILE} build

up:  ## Up docker-compose
	docker-compose -f ${LOCAL_COMPOSE_FILE} -p bot up

down:  ## Down docker-compose
	docker-compose -f ${LOCAL_COMPOSE_FILE} -p bot down --volumes --remove-orphans

sh:  ## Run ipython
	docker-compose -f ${LOCAL_COMPOSE_FILE} -p bot exec app ipython
