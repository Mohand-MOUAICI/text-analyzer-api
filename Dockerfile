FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY . .

# Mettre à jour pip
RUN pip install --upgrade pip

# Installer les dépendances
RUN pip install -r requirements.txt && \
    python -m spacy download en_core_web_sm

# Exposer le port de l'API
EXPOSE 8000

# Commande de lancement
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
