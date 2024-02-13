# main.py
from decoupage import main_decoupage
from vectoriser import vectoriser
from cos_sin import cos_sin
import subprocess
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

chemin_executable_llama = "/Users/mouadsadik/Projects/llama.cpp/main"
chemin_modele = "/Users/mouadsadik/Projects/llama.cpp/models/openhermes-2.5-mistral-7b.Q4_K_M.gguf"


if __name__ == "__main__":
    
    # Récupérer all_paragraphs
    question = input("Quelle est-ta question : ")
    all_paragraphs = main_decoupage()
    embeddings = vectoriser(all_paragraphs)
    embeded_question = vectoriser(question)
    reponses = cos_sin(all_paragraphs, embeddings, embeded_question)
    print("\n\n\n -------------------------------------------------")
    commande = [
        chemin_executable_llama,
        "-m", chemin_modele,
        "-p", ' Je vais te donner un context à partir de mes fichier que tu vas utiliser pour construire une réponse.\n Voici le contexte : ' + reponses + '.\n Voici ma question :' + question + '\n Réponse : ',
        "-n", "1000",
        "-e" 
         # Active le mode évaluation
    ]

    

    resultat = subprocess.run(commande, capture_output=True, text=True)

    # Affichez la sortie
    print(resultat.stdout)
    


    