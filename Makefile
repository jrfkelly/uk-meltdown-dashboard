# Makefile

.PHONY: init ingest up down logs rebuild

init:
	docker compose run --rm app bash -c "PYTHONPATH=/app python -m init_db"

ingest:
	docker compose run --rm app bash -c "PYTHONPATH=/app python -m collect_gilts"

up:
	docker compose up --build -d

down:
	docker compose down

logs:
	docker compose logs -f app

rebuild:
	docker compose build --no-cache
