# main.py
from decoupage import main_decoupage
from vectoriser import vectoriser
from cos_sin import cos_sin


if __name__ == "__main__":
    
    # Récupérer all_paragraphs
    question = input("Quelle est-ta question : ")
    all_paragraphs = main_decoupage()
    embeddings = vectoriser(all_paragraphs)
    embeded_question = vectoriser(question)
    cos_sin(all_paragraphs, embeddings, embeded_question)
    print(embeddings)
    


    