# %% Imports
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.document import Document
from langchain.embeddings import HuggingFaceEmbeddings
from sentence_transformers import CrossEncoder
from transformers import pipeline
import pandas as pd, random

# %% Add the documents
docs = [
    Document(page_content="Deep learning enables neural networks to analyze complex data like images and speech."),
    Document(page_content="Applications of deep learning include NLP, robotics, and medical imaging."),
    Document(page_content="Convolutional networks are used for image recognition and computer vision tasks."),
    Document(page_content="Recurrent neural networks are suitable for sequential data like text or time series."),
    Document(page_content="Transformers like BERT and GPT revolutionized NLP with self-attention mechanisms."),
    Document(page_content="Deep learning improves automation, prediction, and optimization in various industries."),
    Document(page_content="Unsupervised deep learning discovers hidden data patterns without labels."),
    Document(page_content="AI systems powered by deep learning can outperform humans in many cognitive tasks."),
    Document(page_content="Optimization algorithms like Adam and SGD help train deep neural networks efficiently."),
    Document(page_content="Deep learning models require large datasets and GPU power for effective training."),
]

# %% Initialize FAISS Vector Store
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(docs, embeddings)

# %% Retrieve Top Documents for a Query
query = "What are real-world applications of deep learning?"
retriever = vectorstore.as_retriever(search_kwargs={"k": 10}) # Retrieves the top 10 most similar documents from FAISS using cosine similarity
retrieved_docs = retriever.get_relevant_documents(query)

# %% Apply Reranker
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
pairs = [(query, doc.page_content) for doc in retrieved_docs]
scores = reranker.predict(pairs)

# %% Rank and Display Results
results = list(zip(scores, retrieved_docs))
results.sort(key=lambda x: x[0], reverse=True)

for i, (score, doc) in enumerate(results, 1):
    print(f"Rank {i} | Score: {score:.4f}\n{doc.page_content}\n")

# %% Summarization of Top Results
top_texts = " ".join([doc.page_content for _, doc in results[:3]])
summary_prompt = f"Summarize the key idea of these top documents:\n{top_texts}"

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarizer(summary_prompt, max_length=100,
                     min_length=30, do_sample=False)[0]['summary_text']

print("\n--- Summary of Top Results ---")
print(summary)
