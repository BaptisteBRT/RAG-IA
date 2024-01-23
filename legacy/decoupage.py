import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import PyPDF2
import pdfplumber
import spacy
# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/home/swaggeur/CTP/input/pdfs-input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Charger le modèle de langue français
nlp = spacy.load("fr_core_news_sm")

# Fonction pour extraire le texte d'un fichier pdf
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# Fonction pour extraire des informations détaillées d'un fichier PDF
def extract_info_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            text += page.extract_text()
            # Vous pouvez également extraire d'autres informations telles que les images, les coordonnées du texte, etc.
    return text

def tokenize_text(text):
    doc = nlp(text)
    paragraphs = []
    current_paragraph = []
    current_token_count = 0
    
    for token in doc:
        # Ignorer les espaces et les retours à la ligne
        if not token.is_space and not token.text.isspace():
            if current_token_count + len(token) <= 300:
                current_paragraph.append(token.text)
                current_token_count += len(token)
            else:
                paragraphs.append(' '.join(current_paragraph))
                current_paragraph = [token.text]
                current_token_count = len(token)
    
    paragraphs.append(' '.join(current_paragraph))
    return paragraphs


def main():
    # Spécifiez le chemin vers le dataset
    dataset_path = "/home/swaggeur/CTP/input/pdfs-input"

    # Liste des fichiers dans le dataset
    files = os.listdir(dataset_path)

    # Liste pour stocker les paragraphes de tous les fichiers
    all_paragraphs = []

    # Parcourir tous les fichiers du dataset et appliquer les fonctions d'extraction
    for file_name in files:
        file_path = os.path.join(dataset_path, file_name)
        text_content = extract_info_from_pdf(file_path)
        paragraphs = tokenize_text(text_content)
        all_paragraphs.extend(paragraphs)

    # Retourner la variable all_paragraphs à la fin de la fonction
    return all_paragraphs


# Si le script est exécuté directement, appeler la fonction main()
if __name__ == "__main__":
    main()