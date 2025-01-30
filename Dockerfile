# Build stage
FROM python:3.11 as builder

# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

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
FROM python:3.11 as final

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PLAYWRIGHT_BROWSERS_PATH=/app/ms-playwright

# Install system dependencies
RUN apt-get update && apt-get install -y \
    cron \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers and dependencies
RUN playwright install --with-deps chromium

# Copy application code
COPY . .

RUN chmod +x ./initial_script.sh

CMD ["sh", "-c", "cron && ./initial_script.sh"]