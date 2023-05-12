help: ## - Получить информацию о командах
	@sed \
		-e '/^[a-zA-Z0-9_\-]*:.*##/!d' \
		-e 's/:.*##\s*/:/' \
		-e 's/^\(.\+\):\(.*\)/$(shell tput setaf 6)\1$(shell tput sgr0):\2/' \
		$(MAKEFILE_LIST) | column -c2 -t -s :

network: ## - Создать общую сеть для сервисов
	docker network create custom_network

run: ## - Запустить docker-compose
	docker-compose -f docker-compose.yaml up --build -d auth

db: ## - Выполнить миграции
	docker-compose -f docker-compose.yaml exec auth bash -c "cd /opt/auth/src && python -m flask db upgrade"

auth_service: ## - Запустить сервис auth
	make run
	make db

stop: ## - Уронить docker-compose
	docker-compose -f docker-compose.yaml down

tests: ## - Запуск контейнеров для тестов и выполнение тестов
	docker-compose -f docker-compose.yaml up --build -d test-db-auth && docker-compose -f docker-compose.yaml up --build -d test-redis-auth
	bash -c "cd auth/src && python -m pytest -p no:cacheprovider ../tests/src/api/*"


clean: ## - Очистить docker
	docker stop $$(docker ps -aq)
	docker rm $$(docker ps -aq)
	docker rmi $$(docker images -q)
