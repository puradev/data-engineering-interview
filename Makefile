# Define the default target, which will be executed when you run `make` without any arguments
.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down

# Define the target for opening a shell
.PHONY: shell
shell:
	docker-compose up -d && docker-compose exec -it app bin/bash