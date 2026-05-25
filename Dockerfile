# Dockerfile for Project NIA

FROM ubuntu:noble

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    lua5.4 \
    quickjs \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Run setup script
RUN chmod +x setup.sh && ./setup.sh

# Default command
CMD ["/bin/bash"]
