import chromadb
# 1. In-memory ChromaDB client — no disk, perfect for testing
client = chromadb.Client()
# 2. Create a collection — like a database table for vectors
collection = client.create_collection(name="company_docs")
# 3. Add documents — ChromaDB auto-generates embeddings
collection.add(
    documents=[
        "The SLA for P1 incidents requires resolution within 15 minutes.",
        "P2 incidents must be resolved within 4 hours of detection.",
        "All employees must submit leave requests 5 days in advance.",
        "The office kitchen closes at 6pm on weekdays.",
        "Critical production errors must be escalated to the on-call engineer immediately.",
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"],
)
# 4. Query — semantic search
results = collection.query(
    query_texts=["How long do we have to fix a critical incident?"],
    n_results=2,
)
print("Query: How long do we have to fix a critical incident?")
print()
print("Top results:")
for i, doc in enumerate(results["documents"][0]):
    print(f"  {i+1}. {doc}")