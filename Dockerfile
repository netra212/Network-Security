FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

# Install system dependencies needed for awscli and pip
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

# Copy app files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run your app
CMD ["python3", "app.py"]
