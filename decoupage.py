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

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# Spécifiez le chemin vers le dataset
dataset_path = "/home/swaggeur/CTP/input/pdfs-input"

# Liste des fichiers dans le dataset
files = os.listdir(dataset_path)

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
            if current_token_count + len(token) <= 512:
                current_paragraph.append(token.text)
                current_token_count += len(token)
            else:
                paragraphs.append(' '.join(current_paragraph))
                current_paragraph = [token.text]
                current_token_count = len(token)
    
    paragraphs.append(' '.join(current_paragraph))
    return paragraphs


# Liste pour stocker les paragraphes de tous les fichiers
# Charger le modèle de langue français
nlp = spacy.load("fr_core_news_sm")
all_paragraphs = []

# Parcourir tous les fichiers du dataset et appliquer les fonctions d'extraction
for file_name in files:
    file_path = os.path.join(dataset_path, file_name)
    text_content = extract_text_from_pdf(file_path)
    # Faites quelque chose avec le texte extrait, par exemple, le sauvegarder dans un autre format ou effectuer une analyse supplémentaire
    # print(f"Contenu extrait du fichier {file_name} :\n{text_content[:300]}...\n")
    
    paragraphs = tokenize_text(text_content)
    
    # Ajouter les paragraphes à la liste globale
    all_paragraphs.extend(paragraphs)

# Afficher les premiers paragraphes (vous pouvez ajuster selon vos besoins)
for i, paragraph in enumerate(all_paragraphs[:5]):
    print(f"Paragraphe {i+1} :\n{paragraph}\n")