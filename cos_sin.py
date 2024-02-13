# cos_sin.py
from scipy import spatial
from operator import itemgetter

def cos_sin(all_paragraphs, embeddings, question):
    cosine_list = []
    reponses = []

    for index_sentence, xt in enumerate(embeddings):
        result = 1 - spatial.distance.cosine(question, xt)
        cosine_list.append({'res': result, 'i': index_sentence})

    cosine_list.sort(key=itemgetter('res'), reverse=True)
    for indice, row in enumerate(cosine_list):
        reponses.append(all_paragraphs[cosine_list[indice]['i']])
        if indice + 1 == 3:
            break

    return '\n'.join(reponses)
