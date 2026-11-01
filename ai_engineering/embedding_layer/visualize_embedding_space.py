# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Define the words 
words = ['king', 'queen', 'man', 'woman', 'boy', 'girl']

# Function to load GloVe embeddings
def load_glove_embeddings(file_path):
    embeddings = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            values = line.strip().split()
            word = values[0]
            vector = np.asarray(values[1:], dtype='float32')
            embeddings[word] = vector
    return embeddings

glove_embeddings = load_glove_embeddings('data.txt') 

embedding_vectors = []
for word in words:
    if word in glove_embeddings:
        embedding_vectors.append(glove_embeddings[word])

embedding_vectors = np.array(embedding_vectors)

# Use t-SNE for dimensionality reduction to 2D
tsne = TSNE(n_components=2, random_state=42, perplexity=2)
reduced_embeddings_tsne = tsne.fit_transform(embedding_vectors)

# Plot the words in the 2D space
plt.figure(figsize=(8, 6))
for i, word in enumerate(words):
    plt.scatter(reduced_embeddings_tsne[i, 0], reduced_embeddings_tsne[i, 1])
    plt.text(reduced_embeddings_tsne[i, 0] + 0.1, reduced_embeddings_tsne[i, 1] + 0.1, word, fontsize=12)

plt.title('Word Embeddings Visualization (2D)')
plt.show()