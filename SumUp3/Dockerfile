FROM python:3.11-slim

WORKDIR /app

COPY data/ /app/data/
COPY scripts/ /app/scripts/
COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y \
    libsqlite3-dev \
    build-essential \
    sqlite3

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["sh", "-c", "python /app/scripts/main.py && exec /bin/bash"]
