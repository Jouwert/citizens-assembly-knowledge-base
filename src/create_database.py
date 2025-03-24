import json
import os
import sys
import chromadb
from chromadb.utils import embedding_functions

# Define paths
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
RESOURCES_PATH = os.path.join(DATA_DIR, "resources.json")
DB_PATH = os.path.join(DATA_DIR, "chroma_db")

def load_resources():
    """Load resources from JSON file."""
    with open(RESOURCES_PATH, 'r') as f:
        data = json.load(f)
    return data["resources"]

def create_database():
    """Create a ChromaDB database with embeddings for the resources."""
    # Load resources
    resources = load_resources()
    
    # Create embedding function
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    # Initialize ChromaDB client
    client = chromadb.PersistentClient(path=DB_PATH)
    
    # Create collection
    collection = client.create_collection(
        name="citizens_assemblies",
        embedding_function=sentence_transformer_ef,
        metadata={"description": "Citizens' Assembly resources worldwide"}
    )
    
    # Prepare data for insertion
    ids = [str(resource["id"]) for resource in resources]
    documents = [
        f"Title: {resource['title']}\n"
        f"Author: {resource['author']}\n"
        f"Geographic Focus: {resource['geographic_focus']}\n"
        f"Topics: {', '.join(resource['topics'])}\n"
        f"Summary: {resource['summary']}"
        for resource in resources
    ]
    metadatas = [
        {
            "title": resource["title"],
            "author": resource["author"],
            "publication_date": resource["publication_date"],
            "url": resource["url"],
            "type": resource["type"],
            "geographic_focus": resource["geographic_focus"],
            "topics": ", ".join(resource["topics"])
        }
        for resource in resources
    ]
    
    # Add documents to collection
    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas
    )
    
    print(f"Created database with {len(resources)} resources.")
    return collection

def query_example(collection):
    """Run a sample query to test the database."""
    # Query for resources related to climate change
    results = collection.query(
        query_texts=["climate change initiatives in Europe"],
        n_results=3
    )
    
    print("\nSample Query Results:")
    for i, (id, document, metadata) in enumerate(zip(
        results["ids"][0], 
        results["documents"][0],
        results["metadatas"][0]
    )):
        print(f"\nResult {i+1}:")
        print(f"ID: {id}")
        print(f"Title: {metadata['title']}")
        print(f"Geographic Focus: {metadata['geographic_focus']}")
        print(f"URL: {metadata['url']}")

if __name__ == "__main__":
    print("Creating Citizens' Assembly Knowledge Base...")
    collection = create_database()
    query_example(collection)
    print("\nDatabase setup complete!")
