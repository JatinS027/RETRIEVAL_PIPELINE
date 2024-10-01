from sentence_transformers import SentenceTransformer, util

# Load embedding model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Encode query and passages
query_embedding = model.encode("What is the capital of France?")
passage_embeddings = model.encode(["Paris is the capital of France.", "Berlin is the capital of Germany."])

# Use cosine similarity to get top-k passages
top_k = util.semantic_search(query_embedding, passage_embeddings, top_k=5)
print(top_k)
