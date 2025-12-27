FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# системные пакеты — ОТДЕЛЬНО
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# python-зависимости — ОТДЕЛЬНО
COPY elochka_final/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# код
COPY elochka_final/ .

CMD ["gunicorn", "elochka_final.wsgi:application", "--bind", "0.0.0.0:8000"]
