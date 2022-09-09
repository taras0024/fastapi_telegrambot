.PHONY: help

help: ## This help dialog.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

LOCAL_COMPOSE_FILE ?= ./docker/docker-compose.yml

# ----------------------------------------------------------------------------------------------------------------------
#                                           LOCAL
# ----------------------------------------------------------------------------------------------------------------------
up:  ## Run docker-compose
	docker-compose -f ${LOCAL_COMPOSE_FILE} -p bot up -d

down:  ## Down docker-compose
	docker-compose -f ${LOCAL_COMPOSE_FILE} -p bot down --volumes --remove-orphans
