import pandas as pd
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# ============================================
# Step 1: Load your Gita dataset
# ============================================
gita_df = pd.read_csv("cleaned_dataset.csv")

# ============================================
# Step 2: Load the better sentence transformer
# ============================================
model = SentenceTransformer("all-mpnet-base-v2")

# ============================================
# Step 3: Combine Question + Answer
# ============================================
combined_corpus = gita_df["Cleaned_Question"] + " " + gita_df["Answer"]

# ============================================
# Step 4: Create new embeddings
# ============================================
corpus_embeddings = model.encode(combined_corpus.tolist(), normalize_embeddings=True).astype('float32')

# Save embeddings for later reference
with open("corpus_embeddings.pkl", "wb") as f:
    pickle.dump(corpus_embeddings, f)

# ============================================
# Step 5: Create FAISS index
# ============================================
dimension = corpus_embeddings.shape[1]  # Size of embedding vector
faiss_index = faiss.IndexFlatL2(dimension)
faiss_index.add(corpus_embeddings)

# Save FAISS index
faiss.write_index(faiss_index, "gita_faiss.index")

print("✅ Embeddings and FAISS index rebuilt successfully!")
