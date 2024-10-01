from sklearn.metrics import ndcg_score

# True relevance (1 if relevant, 0 if not relevant)
true_relevance = [[1, 0, 0, 1, 0]]  # Ground truth relevance for top-5 results

# Model's predicted scores for top-5 passages
scores = [[0.8, 0.5, 0.3, 0.9, 0.2]]

# Calculate NDCG@10
ndcg = ndcg_score(true_relevance, scores, k=10)
print(f"NDCG@10: {ndcg}")
