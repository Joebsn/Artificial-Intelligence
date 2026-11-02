# Embedding layer

The embedding layer converts high-dimensional or categorical data into lower-dimensional numerical vectors that capture meaningful patterns and relationships.

## Working (explanation 1)

### Define similarity signal

First, decide what we want the model to treat as “similar”.

- Text: Words or sentences that appear in similar contexts.
- Images: Pictures of the same object or scene.
- Graphs: Nodes that are connected or related.

### Choose dimensionality

Select how many numbers (dimensions) will describe each item, it could be 64, 384, 768 or more.

- More dimensions: more detail but slower and uses more memory.
- Fewer dimensions: faster but may lose detail.

### Build the encoder

This is the model that turns our data into a list of numbers (vector):

- Text: Language models like BERT.
- Images: Vision models like CNN or ViT.
- Audio: Models that process sound (e.g., turning it into spectrograms first).
- Graphs: Methods like Node2Vec or graph neural networks.
- Tabular data: Models that compress features into embeddings.

### Train with a metric learning objective

Show the model examples of things that are “similar” and “different.”
Teach it to place similar ones close together and different ones far apart.
This process is called metric learning.

### Negative sampling and batching

Give the model tricky “hard negative” examples, things that seem alike but aren’t so it learns to tell them apart better.

### Validate and Tune

Test how well our embeddings work by checking:

How accurate search results are.
How well items group into the right categories.
How good automatic clustering is.

### Index for Fast Retrieval

Store our vectors in a special database like Qdrant or FAISS to quickly find the closest matches, even from millions of items.

### Use the embeddings

Once ready, embeddings can be used for:

- Semantic search: finding by meaning, not exact words.
- RAG (Retrieval-Augmented Generation): feeding relevant facts to an AI model.
- Classification: predicting the correct label or category.
- Clustering: grouping similar items together.
- Recommendations: suggesting similar products, content or users.
- Monitoring: spotting unusual changes or patterns over time.

## Working (explanation 2)

### Input Representation

Suppose we have a sentence containing words such as "cat", "dog" and "apple". Each word is assigned a unique integer ID based on the vocabulary.

### Embedding Mapping

The embedding layer maps each word ID to a dense numerical vector. Instead of representing "cat" as a single number, it represents it as a vector such as [0.2, 0.8, -0.5]. Similarly, "dog" could be represented as [0.3, 0.7, -0.6]. The values in these vectors are learned during model training.

### Learning Relationships

During training, the model updates the embedding vectors based on the training objective. Words that occur in similar contexts may develop similar vector representations, allowing the model to capture useful relationships between words.

![alt text](image.png)

### Example of Learning Relationships

- Consider the sentence "The cat chased the mouse."
- Across many training examples, the model learns from the contexts in which words such as "cat", "dog" and "mouse" appear.
- If "cat" and "dog" occur in similar contexts, their embedding vectors may become more similar, allowing the model to capture relationships between them in the embedding space.

## T-distributed Stochastic Neighbor Embedding (t-SNE) Algorithm - ML

T-distributed Stochastic Neighbor Embedding (t-SNE) is a non linear dimensionality reduction technique used for visualizing high-dimensional data in a lower-dimensional space mainly in 2D or 3D. Unlike linear methods such as Principal Component Analysis (PCA), t-SNE focus on preserving the local structure and pattern of the data.

- Dimensionality reduction is a process that simplifies complex dataset by combining similar or correlated features.
- It helps in improving analysis and computational efficiency.
- t-SNE works by looking at the similarity between data points in the high-dimensional space.
- The similarity is computed as a conditional probability. It calculates how likely it is that one data point would be near another.
