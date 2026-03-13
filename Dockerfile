FROM ubuntu:22.04

# Avoid interactive prompts during package installs
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and pip
RUN apt-get update \
 && apt-get install -y --no-install-recommends python3 python3-pip \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Flask defaults
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["python3", "app.py"]
