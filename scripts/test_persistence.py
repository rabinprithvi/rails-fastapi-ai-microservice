# open peristence db

import chromadb


client = chromadb.PersistentClient(path="./chroma_data")

#get collections
policy_collection = client.get_collection(name="policy")
errors_collection = client.get_collection(name="errors")

print(f"Policy collection: {policy_collection.count()} chunks")
print(f"Errors collection: {errors_collection.count()} chunks")

print("\n--- Query: 'What happens if P1 is not resolved in time?' ---")
results = policy_collection.query(
    query_texts = ["What happens if P1 is not resolved in time?"],
    n_results = 2,
    include=["documents", "distances", "metadatas"],
)

for doc, dist, meta in zip(
    results["documents"][0],
    results["distances"][0],
    results["metadatas"][0],
):
    print(f"  Distance {dist:.3f} | Meta: {meta} | {doc[:80]}...")

print("\n--- Query: 'What caused the checkout failure?' ---")

results = errors_collection.query(
    query_texts=["What caused the checkout failure?"],
    n_results=2,
    include=["documents", "distances", "metadatas"],
)
for doc, dist, meta in zip(
    results["documents"][0],
    results["distances"][0],
    results["metadatas"][0],
):
    print(f"  Distance {dist:.3f} | Meta: {meta} | {doc[:80]}...")


