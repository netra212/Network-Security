FROM python:3.10-slim-bookworm

WORKDIR /app

# Install system dependencies for awscli and pip
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    unzip \
    less \
    groff \
    awscli \
    ca-certificates \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
