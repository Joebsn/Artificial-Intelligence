# %% Import libraries
import numpy as np
import smart_open
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import gensim.downloader as api
from gensim.models import Word2Vec

# %% Load Data and Train Word2Vec Model
smart_open.smart_open = smart_open.open
corpus = api.load('text8')
model = Word2Vec(corpus)

# %% Select Words and Get Their Embeddings
words = ['cat', 'dog', 'elephant', 'lion', 'bird', 'rat', 'wolf', 'cow',
         'goat', 'snake', 'rabbit', 'human', 'parrot', 'fox', 'peacock',
         'lotus', 'roses', 'marigold', 'jasmine', 'computer', 'robot',
         'software', 'vocabulary', 'machine', 'eye', 'vision',
         'grammar', 'words', 'sentences', 'language', 'verbs', 'noun',
         'transformer', 'embedding', 'neural', 'network', 'optimization']

# Extracts their vector representations from the model as NumPy arrays.
words = [word for word in words if word in model.wv.key_to_index]
word_embeddings = [model.wv[word] for word in words]
embeddings = np.array(word_embeddings)
print(embeddings)
print(embeddings.shape)

# %% Reduce Dimensionality with t-SNE
# (Uses t-SNE from scikit learn to shrink high dimensional word vectors into
# two dimensions for visualization.)
tsne = TSNE(n_components=2, perplexity=2)
embeddings_2d = tsne.fit_transform(embeddings)
print(embeddings_2d)
print(embeddings_2d.shape)

# %% Plot Embedding
plt.figure(figsize=(10, 7), dpi=1000)
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], marker='o')
for i, word in enumerate(words):
    plt.text(embeddings_2d[i, 0], embeddings_2d[i, 1],
             word, fontsize=10, ha='left', va='bottom')
plt.xlabel('t-SNE Dimension 1')
plt.ylabel('t-SNE Dimension 2')
plt.title('Word Embedding Graph (t-SNE with Word2Vec)')
plt.grid(True)
plt.savefig('embedding.png')
plt.show()
