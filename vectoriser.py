from sentence_transformers import SentenceTransformer

def vectoriser(paragraphs):

    model = SentenceTransformer('intfloat/multilingual-e5-base')
    embeddings = model.encode(paragraphs, normalize_embeddings=True)
    return embeddings