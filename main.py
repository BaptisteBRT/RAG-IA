# main.py
from decoupage import main_decoupage
from vectoriser import vectoriser

if __name__ == "__main__":
    
    # Récupérer all_paragraphs
    all_paragraphs = main_decoupage()
    embeddings = vectoriser(all_paragraphs)
    print(embeddings)

    