from sentence_transformers import SentenceTransformer

def vectoriser(paragraphs):

    model = SentenceTransformer('intfloat/multilingual-e5-base')
    embeddings = model.encode(input_texts, normalize_embeddings=True)
    return embeddings