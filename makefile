ROJECT_NAME := docker-reverse-proxy-challenge

up:
	docker-compose up --build -d

down:
	docker-compose down

logs:
	docker-compose logs -f

clean: #remove containers, volumes e img nao usadas
	docker-compose down --rmi all -v --remove-orphans
	docker image prune -f

help:
	@echo "Comandos disponíveis:"
	@echo "  make up    - Constrói as imagens e inicia os containers em background."
	@echo "  make down  - Para e remove containers e redes."
	@echo "  make logs  - Exibe os logs de todos os containers em tempo real."
	@echo "  make clean - Para, remove containers, volumes e imagens."

.PHONY: up down logs clean help