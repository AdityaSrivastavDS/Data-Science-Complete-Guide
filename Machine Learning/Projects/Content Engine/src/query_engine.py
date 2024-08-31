from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.query_engine import LangChainQueryEngine

# Initialize Pinecone Vector Store
vector_store = Pinecone(index)

# Set up LangChain Query Engine
query_engine = LangChainQueryEngine(vector_store, OpenAIEmbeddings())

def query_documents(query):
    return query_engine.query(query)
