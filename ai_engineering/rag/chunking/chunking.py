# %% Define imports and methods
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter, TokenTextSplitter
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader

text = open("RAG/chunking/document.txt", "r").read()

def _print_chunks(chunks):
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {len(chunk)} characters")
        print(chunk)

def _split_text_and_print(splitter, mode):
    print(f"--- {mode} ---")
    chunks = splitter.split_text(text)
    _print_chunks(chunks)

# %% Fixed Size Chunking
_split_text_and_print(CharacterTextSplitter(chunk_size=300, chunk_overlap=50),
                      "Fixed Size Chunking")

# %% Recursive Character Chunking
_split_text_and_print(RecursiveCharacterTextSplitter(chunk_size=400,chunk_overlap=80,separators=["\n\n", "\n", " ", ""]),
                      "Recursive Character Chunking")

#%% Token Based Chunking
_split_text_and_print(TokenTextSplitter(chunk_size=256, chunk_overlap=32),
                      "Token Based Chunking")

# %% Sentence / Semantic Chunking
embeddings = OpenAIEmbeddings()
_split_text_and_print(SemanticChunker(embeddings=embeddings),
                      "Sentence / Semantic Chunking")

# %% Document based chunking
print(f"--- Document based chunking ---")
loader = TextLoader("document.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(documents)
_print_chunks(chunks)