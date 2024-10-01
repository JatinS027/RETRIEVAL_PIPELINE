from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load ranking model
tokenizer = AutoTokenizer.from_pretrained('cross-encoder/ms-marco-MiniLM-L-12-v2')
model = AutoModelForSequenceClassification.from_pretrained('cross-encoder/ms-marco-MiniLM-L-12-v2')

# Rerank the retrieved passages
inputs = tokenizer("What is the capital of France? [SEP] Paris is the capital of France.", return_tensors="pt")
scores = model(**inputs).logits
print(scores)
