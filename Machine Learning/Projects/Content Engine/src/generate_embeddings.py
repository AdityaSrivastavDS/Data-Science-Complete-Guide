from sentence_transformers import SentenceTransformer

# Load Embedding Model
model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(text):
    return model.encode([text])
