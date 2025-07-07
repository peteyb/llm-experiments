FROM python:3.13.3-slim-bookworm

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# Enable bytecode compilation for better performance
ENV UV_COMPILE_BYTECODE=1

# Copy project files for dependency installation
COPY pyproject.toml .
COPY README.md .
COPY uv.lock .

# Install dependencies using uv
RUN uv sync --frozen --no-install-project

# Copy the entire app directory
COPY app ./app/
COPY run.py .

# Run with uv
CMD ["uv", "run", "python", "run.py"]
