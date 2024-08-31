from parse_documents import extract_text_from_pdf
from generate_embeddings import create_embeddings
from store_vectors import store_embeddings
from query_engine import query_documents
from local_llm import generate_response

# Paths to PDF files
pdf_paths = ["data/Alphabet_10-K.pdf", "data/Tesla_10-K.pdf", "data/Uber_10-K.pdf"]

# Process each PDF
for pdf_path in pdf_paths:
    text = extract_text_from_pdf(pdf_path)
    embeddings = create_embeddings(text)
    store_embeddings(pdf_path, embeddings)

# Example Query
query = "What are the risk factors associated with Google and Tesla?"
response = query_documents(query)
print(response)
