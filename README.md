# SASS pdf-to-text

## Structure du projet

```
pdf-to-text-docker
├── app/
│   ├── main.py          # Application Flask
│   ├── requirements.txt # Dépendances
├── Dockerfile           # Fichier Docker
└── README.md
```

## Commandes pour builder

```bash
# Construire l'image Docker
docker build -t pdf-to-docx .

# Exécuter le conteneur
docker run -p 5000:5000 pdf-to-docx
```

### Explication du code

* pdf_to_text() : Utilise pdf2image pour convertir chaque page du PDF en image, puis pytesseract pour extraire le texte de chaque image.
* save_text_to_docx() : Prend le texte extrait et le sauvegarde dans un fichier DOCX en utilisant python-docx.
* **Paramètre** format : Le paramètre format est récupéré depuis le formulaire pour déterminer si l’utilisateur souhaite le texte brut ou un fichier DOCX.
* **Retour JSON pour le texte** : Si le format spécifié est text, le texte extrait est renvoyé directement en JSON.
* **Envoi du fichier DOCX** : Si le format est docx (ou si le paramètre est omis), le fichier DOCX est généré puis envoyé en pièce jointe.


Cette structure devrait être une bonne base pour votre système SASS. Vous pouvez adapter et enrichir le code selon vos besoins.

Pour vous permettre de choisir entre la récupération du texte brut ou du fichier DOCX, je vais modifier l'application pour inclure une option de format dans la requête. Vous pourrez spécifier soit text pour obtenir le texte brut, soit docx pour télécharger le fichier DOCX.

## Commandes pour tester l'application

> Ne pas oublier de décommenter la ligne **# EXPOSE 5000** dans le fichier **Dockerfile** pour rendre accessible l'applicatif.

```bash
# Construire l'image Docker
docker build -t pdf-to-docx .

# Exécuter le conteneur
docker run -p 5000:5000 pdf-to-docx
```

* **Pour le texte brut:**
```bash
curl -F "file=@path/to/your/file.pdf" -F "format=text" http://localhost:5000/upload

```

* ** Pur le fichier DOCX:**
```bash
curl -F "file=@path/to/your/file.pdf" -F "format=docx" http://localhost:5000/upload -o output.docx
```

## Pour utiliser la partie SASS avec docker compose

```bash
## LINK .env FILE
ln -s ./env.detail .env

## BUILD
docker compose build

## RUN
docker compose up -d

## DOWN
docker compose down
```

## Pour tester l'applicatif, les commandes deviennent:

```bash
## Pour le texte brut
curl -F "file=@./test/Physio-Energie_W10_Le-système-endocrinien.pdf" -F "format=text" https://pdfconv.docker.localhost/upload

## Pour la version docx
curl -F "file=@./test/Physio-Energie_W10_Le-système-endocrinien.pdf" -F "format=docx" https://pdfconv.docker.localhost/upload -o output.docx
```
