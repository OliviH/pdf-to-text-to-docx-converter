# Utiliser une image Python
FROM python:3.9-slim

# Installer les dépendances système
RUN apt-get update && \
    apt-get install -y tesseract-ocr poppler-utils && \
    apt-get clean

# Installer les dépendances Python
COPY app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copier le code source
COPY app /app
WORKDIR /app

# Créer les dossiers nécessaires
RUN mkdir -p /app/uploads /app/output

# Exposer le port Flask Uncomment
# EXPOSE 5000

# Lancer l'application
CMD ["python", "main.py"]
