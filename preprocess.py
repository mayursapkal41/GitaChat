import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Load your dataset
gita_df = pd.read_csv("cleaned_dataset.csv")

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Embed the Cleaned Questions
corpus = gita_df["Cleaned_Question"].tolist()
corpus_embeddings = model.encode(corpus, normalize_embeddings=True)

# Save the corpus embeddings
with open("corpus_embeddings.pkl", "wb") as f:
    pickle.dump(corpus_embeddings, f)

# Create FAISS Index
dimension = corpus_embeddings.shape[1]  # Should be 384 for MiniLM
index = faiss.IndexFlatL2(dimension)
index.add(np.array(corpus_embeddings).astype('float32'))

# Save FAISS index
faiss.write_index(index, "gita_faiss.index")

print("✅ Preprocessing Done. FAISS index created!")
