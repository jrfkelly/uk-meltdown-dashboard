# Dockerfile

FROM python:3.11-slim

# set working directory
WORKDIR /app

# install system deps (for pandas, psycopg2)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY app/ app/
COPY .env .

# default cmd
CMD ["python", "dashboard.py"]
