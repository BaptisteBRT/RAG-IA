import pdfplumber
import re
import os

def clean_spaces(text):
    # Nettoyer les espaces en trop
    cleaned_text = re.sub('\s+', ' ', text)
    return cleaned_text

def split_into_paragraphs(text, paragraph_length=300):
    # Diviser le texte en paragraphes d'environ 300 mots
    words = text.split()
    paragraphs = []
    current_paragraph = words[0]

    for word in words[1:]:
        if len(current_paragraph) + len(word) + 1 <= paragraph_length:
            current_paragraph += ' ' + word
        else:
            paragraphs.append(current_paragraph)
            current_paragraph = word

    paragraphs.append(current_paragraph)
    return paragraphs

def process_pdf(file_path):
    # Lire le contenu du PDF
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            text += page.extract_text()
    # Nettoyer les espaces
    cleaned_text = clean_spaces(text)

    # Diviser en paragraphes
    paragraphs = split_into_paragraphs(cleaned_text)

    return paragraphs

def process_multiple_pdfs(folder_path):
    # Obtenir la liste des fichiers PDF dans le dossier
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # Tableau pour stocker tous les paragraphes 
    all_paragraphs = []

    # Traiter chaque fichier PDF
    for pdf_file in pdf_files:
        pdf_file_path = os.path.join(folder_path, pdf_file)
        result = process_pdf(pdf_file_path)

        # Ajouter les paragraphes au tableau global
        all_paragraphs.extend(result)

    return all_paragraphs

def main_decoupage():
    # Exemple d'utilisation avec un dossier contenant les fichiers PDF
    pdf_folder_path = '/home/swaggeur/CTP/input/pdfs-input'
    return process_multiple_pdfs(pdf_folder_path)


# Si le script est exécuté directement, appeler la fonction main()
if __name__ == "__main__":
    all_paragraphs = main_decoupage()

    # Maintenant, vous pouvez utiliser la variable all_paragraphs comme vous le souhaitez
    print("Nombre total de paragraphes :", len(all_paragraphs))

    for i, paragraph in enumerate(all_paragraphs[:10]):
        print(f"Paragraphe {i+1} :\n{paragraph}\n")
