FROM python:3.11-slim

WORKDIR /app

COPY requirements_prod.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements_prod.txt

COPY . .

EXPOSE 8000
EXPOSE 8501