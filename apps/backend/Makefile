.PHONY: help install dev-install sync run run-local test lint format clean docker-build docker-run docker-dev

help:
	@echo "Available commands:"
	@echo "  install       - Install production dependencies"
	@echo "  dev-install   - Install development dependencies"
	@echo "  sync          - Sync all dependencies from lock file"
	@echo "  run           - Run the application with Docker"
	@echo "  run-local     - Run the application locally"
	@echo "  test          - Run tests"
	@echo "  lint          - Run linting"
	@echo "  format        - Format code"
	@echo "  clean         - Remove cache and build artifacts"
	@echo "  docker-build  - Build Docker image"
	@echo "  docker-run    - Run Docker container"
	@echo "  docker-dev    - Run Docker container with hot reload for development"

install:
	uv sync --no-dev

dev-install:
	uv sync

sync:
	uv sync --frozen

run: docker-dev

run-local:
	uv run uvicorn app.main:app --host 0.0.0.0 --port 8900 --reload

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run mypy app

format:
	uv run ruff check . --fix
	uv run black .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	rm -rf .coverage htmlcov

docker-build:
	docker build -t llm-experiments-backend -f docker/Dockerfile .

docker-run:
	docker run -p 8900:8900 --env-file .env llm-experiments-backend

docker-dev:
	docker run -p 8900:8900 --env-file .env -v $(PWD)/app:/app/app --rm llm-experiments-backend uv run uvicorn app.main:app --host 0.0.0.0 --port 8900 --reload
	docker run -p 8000:8900 --env-file .env llm-experiments-backend