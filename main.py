# main.py
from decoupage import main

if __name__ == "__main__":
    # Appeler la fonction main du module des dépendances et récupérer all_paragraphs
    all_paragraphs = main()

    # Maintenant, vous pouvez utiliser la variable all_paragraphs comme vous le souhaitez
    print("Nombre total de paragraphes :", len(all_paragraphs))
    # Afficher les premiers paragraphes (vous pouvez ajuster selon vos besoins)
    for i, paragraph in enumerate(all_paragraphs[:5]):
        print(f"Paragraphe {i+1} :\n{paragraph}\n")
