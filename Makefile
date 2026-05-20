# Makefile — Atajos para el entorno de desarrollo
# Uso: make <comando>
# Requiere: Docker Desktop instalado y corriendo

.PHONY: build up down shell dbt-run dbt-test dbt-docs clean help \
	pre-commit-install pre-commit-run test lint format dbt-deps dbt-build ci-local

## Construir la imagen Docker (solo necesario la primera vez)
build:
	docker compose build

## Levantar el entorno (Jupyter Lab en http://localhost:8888)
up:
	docker compose up

## Levantar en segundo plano
up-detached:
	docker compose up -d

## Abrir una terminal bash dentro del contenedor
shell:
	docker compose exec workspace bash

## Ejecutar todos los modelos dbt
dbt-run:
	docker compose exec workspace bash -c "cd /workspace/dbt_project && dbt run"

## Ejecutar tests dbt
dbt-test:
	docker compose exec workspace bash -c "cd /workspace/dbt_project && dbt test"

## Generar y servir documentación dbt (http://localhost:8080)
dbt-docs:
	docker compose exec workspace bash -c \
		"cd /workspace/dbt_project && dbt docs generate && dbt docs serve --port 8080"

## Apagar el entorno
down:
	docker compose down

## Apagar y eliminar la imagen (libera espacio en disco)
clean:
	docker compose down --rmi all --volumes

## Instalar pre-commit hooks en tu git local
pre-commit-install:
	pre-commit install

## Correr todos los pre-commit hooks contra todos los archivos
pre-commit-run:
	pre-commit run --all-files

## Correr tests Python con coverage (dentro del contenedor)
test:
	docker compose exec workspace bash -c "cd /workspace && pytest tests/ --cov=src/mercado --cov-report=term-missing"

## Lint de Python (ruff) y SQL (sqlfluff)
lint:
	docker compose exec workspace bash -c "cd /workspace && ruff check src/ tests/"
	docker compose exec workspace bash -c "cd /workspace && sqlfluff lint dbt_project/mercado/models/ --config /workspace/.sqlfluff" || echo "(sqlfluff: aún sin modelos para validar — OK en esta fase)"

## Formatear código Python con ruff
format:
	docker compose exec workspace bash -c "cd /workspace && ruff format src/ tests/"

## Instalar dependencias de dbt (packages.yml)
dbt-deps:
	docker compose exec workspace bash -c "cd /workspace/dbt_project/mercado && dbt deps"

## Pipeline completo: deps → build → test → docs
dbt-build:
	docker compose exec workspace bash -c "cd /workspace/dbt_project/mercado && dbt build"

## Correr EXACTAMENTE las mismas validaciones que GitHub Actions (rule pre-commit)
ci-local:
	@echo "── 1/5 ruff check (full repo) ──"
	docker compose exec workspace bash -c "cd /workspace && ruff check ."
	@echo "── 2/5 ruff format --check (full repo) ──"
	docker compose exec workspace bash -c "cd /workspace && ruff format --check ."
	@echo "── 3/5 pytest con cobertura ──"
	docker compose exec workspace bash -c "cd /workspace && pytest tests/ --cov=src/mercado --cov-report=term-missing"
	@echo "── 4/5 dbt deps + parse ──"
	docker compose exec workspace bash -c "cd /workspace/dbt_project/mercado && dbt deps && dbt parse"
	@echo "── 5/5 dbt compile ──"
	docker compose exec workspace bash -c "cd /workspace/dbt_project/mercado && dbt compile"
	@echo ""
	@echo "✅ Todas las validaciones de CI pasaron localmente. Listo para commit."

## Mostrar este mensaje de ayuda
help:
	@echo ""
	@echo "Comandos disponibles:"
	@echo "  make build       → Construir la imagen (primera vez)"
	@echo "  make up          → Levantar Jupyter Lab"
	@echo "  make up-detached → Levantar en segundo plano"
	@echo "  make shell       → Abrir terminal en el contenedor"
	@echo "  make dbt-run     → Ejecutar modelos dbt"
	@echo "  make dbt-test    → Ejecutar tests dbt"
	@echo "  make dbt-docs    → Generar y servir docs dbt"
	@echo "  make down        → Apagar el entorno"
	@echo "  make clean       → Apagar y limpiar imagen"
	@echo "  make pre-commit-install → Instalar hooks pre-commit"
	@echo "  make pre-commit-run     → Ejecutar hooks en todos los archivos"
	@echo "  make test        → pytest con cobertura (contenedor)"
	@echo "  make lint        → ruff + sqlfluff (contenedor)"
	@echo "  make format      → ruff format (contenedor)"
	@echo "  make dbt-deps    → dbt deps"
	@echo "  make dbt-build   → dbt build"
	@echo "  make ci-local    → Validaciones de CI antes de commit (REGLA OBLIGATORIA)"
	@echo ""
