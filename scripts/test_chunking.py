from langchain_text_splitters import RecursiveCharacterTextSplitter

# Sample company policy document
policy_text = """
Section 1: Incident Response Policy
P1 incidents are critical production outages affecting all users. 
They must be resolved within 15 minutes of detection. 
The on-call engineer must be paged immediately.

Section 2: P2 Incident Policy
P2 incidents affect a subset of users or a non-critical system. 
Resolution time is 4 hours from detection. 
A ticket must be filed within 30 minutes.

Section 3: Leave Policy
All employees must submit leave requests at least 5 days in advance.
Emergency leave requires manager approval within 24 hours.
Maximum consecutive leave is 15 days without HR review.

Section 4: Escalation Policy
If a P1 is not resolved within 10 minutes, escalate to the engineering manager.
If unresolved after 15 minutes, escalate to the CTO.
All escalations must be logged in the incident tracker.
"""

# --- Experiment 1: large chunks, no overlap ---
splitter_large = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,
)
chunks_large = splitter_large.split_text(policy_text)

print("=== LARGE CHUNKS (300 chars, 0 overlap) ===")
for i, chunk in enumerate(chunks_large):
    print(f"\nChunk {i+1} ({len(chunk)} chars):\n{chunk}")

# --- Experiment 2: small chunks with overlap ---
splitter_small = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30,
)
chunks_small = splitter_small.split_text(policy_text)

print("\n\n=== SMALL CHUNKS (150 chars, 30 overlap) ===")
for i, chunk in enumerate(chunks_small):
    print(f"\nChunk {i+1} ({len(chunk)} chars):\n{chunk}")

print(f"\nLarge chunks: {len(chunks_large)} | Small chunks: {len(chunks_small)}")