FROM python:3.11-slim

# Empêche Python d'écrire des fichiers .pyc et force l'affichage des logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Installation des dépendances système nécessaires (ex: pour PostgreSQL)
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app/

# On utilisera uvicorn pour lancer FastAPI/Ninja (ou le serveur de dev Django)
# Note: La commande finale est définie dans le docker-compose.yml
EXPOSE 8000
