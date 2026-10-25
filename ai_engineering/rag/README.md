# Retrieval Augmented Generation (RAG)

Retrieval Augmented Generation (RAG) is a technique used to improve the accuracy of AI systems by allowing language models to access external knowledge sources. Instead of relying only on the model’s training data, RAG systems retrieve relevant information from documents or databases before generating a response.
The main components are:

## Chunking

It is used to divide large documents into smaller sections called chunks.This makes it easier for the system to search and retrieve relevant information efficiently.

## Retrieval

When a user asks a question, the system searches the stored document chunks to find the pieces of information that are most relevant to the query using retrieval.

## Reranking

After retrieval, several candidate chunks may be returned. Reranking is the process of re-evaluating these results and ordering them based on their relevance to the query.

## Context Injection

The selected chunks are then added to the prompt that is sent to the language model. This additional context helps the model generate more accurate and informative responses.
