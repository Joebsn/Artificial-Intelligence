# Context engineering

Context engineering focuses on improving how information is selected and presented to language models. Since LLMs have limited context windows, it is important to provide only the most relevant and useful information so the model can generate accurate responses.

## Query Rewriting

Modifying or expanding the user’s query to make it clearer and easier for the retrieval system to find relevant information.

## Multi stage Retrieval

Retrieving documents in multiple steps, where an initial search finds candidate documents and later stages refine the results.

## Context Filtering

Removing irrelevant or low quality information from retrieved results so that only useful content is passed to the model.
Document Ranking: Ordering retrieved documents based on their relevance to the query to ensure the most important information is included in the final context.

## Hybrid Search

It combines keyword search, vector search and semantic ranking to retrieve both exact matches and contextually relevant results. Example: (BM25), vector search and semantic ranking.