FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

RUN mkdir -p /app/migrations/versions && \
    chown -R appuser:appuser /app && \
    chmod -R 777 /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

USER appuser

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
