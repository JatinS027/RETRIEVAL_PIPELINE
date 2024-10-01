from beir import util
from beir.datasets.data_loader import GenericDataLoader
from nltk.tokenize import sent_tokenize

# Step 1: Load BEIR Dataset
url = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/nq.zip"
data_path = util.download_and_unzip(url, "datasets")
corpus, queries, qrels = GenericDataLoader(data_path).load(split="test")

# Step 2: Split large documents into smaller passages
def split_into_passages(text, max_length=512):
    sentences = sent_tokenize(text)
    passages = []
    passage = ""
    for sentence in sentences:
        if len(passage) + len(sentence) <= max_length:
            passage += sentence + " "
        else:
            passages.append(passage.strip())
            passage = sentence
    if passage:
        passages.append(passage.strip())
    return passages

# Example: Splitting a document into smaller passages
document = corpus['doc1']['text']
passages = split_into_passages(document)
print(passages)
