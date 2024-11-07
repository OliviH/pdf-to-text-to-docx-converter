from flask import Flask, request, send_file, jsonify
from pdf2image import convert_from_path
import pytesseract
from docx import Document
import os

app = Flask(__name__)

# Dossier temporaire pour stocker les fichiers convertis
UPLOAD_FOLDER = "/app/uploads"
OUTPUT_FOLDER = "/app/output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Enregistrer le fichier PDF
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Extraire le texte du PDF
    text = pdf_to_text(file_path)

    # Vérifier le format souhaité
    format = request.form.get('format', 'docx')
    
    if format == 'text':
        # Retourner le texte brut
        return jsonify({"text": text})
    elif format == 'docx':
        # Sauvegarder le texte en DOCX
        output_file = os.path.join(OUTPUT_FOLDER, file.filename.rsplit('.', 1)[0] + '.docx')
        save_text_to_docx(text, output_file)
        return send_file(output_file, as_attachment=True)
    else:
        return jsonify({"error": "Invalid format specified. Use 'text' or 'docx'."}), 400

def pdf_to_text(file_path):
    images = convert_from_path(file_path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    return text

def save_text_to_docx(text, output_file):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_file)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
