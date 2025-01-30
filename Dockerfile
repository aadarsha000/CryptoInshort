# Build stage
FROM python:3.11-alpine as builder

# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Install system dependencies needed for building
RUN apk add --no-cache \
  build-base \
  gcc \
  musl-dev \
  jpeg-dev \
  zlib-dev

# Install and configure Poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VERSION=1.4.2
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false
RUN pip install "poetry==${POETRY_VERSION}" poetry-plugin-export

# Set work directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Export dependencies
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# Final stage
FROM python:3.11-alpine as final

# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Install cron and other dependencies
RUN apk add --no-cache dcron libc6-compat poppler-utils

WORKDIR /app

# Copy requirements and install
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

RUN chmod +x ./initial_script.sh

CMD ["sh", "-c", "crond -b && ./initial_script.sh"]