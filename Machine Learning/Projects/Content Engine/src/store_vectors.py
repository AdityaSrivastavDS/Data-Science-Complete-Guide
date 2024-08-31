import pinecone

# Initialize Pinecone
pinecone.init(api_key="your-pinecone-api-key", environment="us-west1-gcp")

# Create Pinecone index
index = pinecone.Index("content-engine")

def store_embeddings(doc_id, embeddings):
    index.upsert([(doc_id, embeddings[0])])
