
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

# client
client = chromadb.PersistentClient(path="./chroma_data")


# delete existing collections
client.delete_collection(name="policy")
client.delete_collection(name="errors")

# create new collections

policy_collection = client.get_or_create_collection(name="policy")
errors_collection = client.get_or_create_collection(name="errors")

# read files
with open("data/policy.txt") as f:
    policy_text = f.read()

with open("data/errors.log") as f:
    errors_text = f.read()

# split both the text to create chunks to ingest in collection
splitter =  RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50 )

policy_chunks = splitter.split_text(policy_text)
errors_chunks = splitter.split_text(errors_text)

# ingest in collection
policy_collection.add(
    documents=policy_chunks,
    ids= [f"policy_{i}" for i in range(len(policy_chunks))],
    metadatas = [{"source": "policy.txt", "type": "policy"} for _ in policy_chunks],
)

errors_collection.add(
    documents=errors_chunks,
    ids=[f"error_{i}" for i in range(len(errors_chunks)) ],
    metadatas = [{"source": "errors.log", "type": "error_log"} for _ in errors_chunks]
)

print(f"Policy chunks stored : {len(policy_chunks)}")
print(f"Error chunks stored  : {len(errors_chunks)}")

# 6. Query policy collection
print("\n--- Query: 'What is the P1 resolution time?' ---")
results = policy_collection.query(
    query_texts=["What is the P1 resolution time?"],
    n_results=2,
    include=["documents", "distances"],
)
for doc, dist in zip(results["documents"][0], results["distances"][0]):
    print(f"  Distance {dist:.3f}: {doc[:80]}...")
# 7. Query errors collection
print("\n--- Query: 'What caused the checkout failure?' ---")
results = errors_collection.query(
    query_texts=["What caused the checkout failure?"],
    n_results=2,
    include=["documents", "distances"],
)
for doc, dist in zip(results["documents"][0], results["distances"][0]):
    print(f"  Distance {dist:.3f}: {doc[:80]}...")

