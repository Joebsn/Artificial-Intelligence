# %% Imports
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, TreebankWordTokenizer, WordPunctTokenizer, RegexpTokenizer
import nltk.data

nltk.download('punkt_tab')

# %% Sentence Tokenization using sent_tokenize
text = "Hello everyone. Welcome to GeeksforGeeks. You are studying NLP article."
print(sent_tokenize(text))

# %% Sentence Tokenization using PunktSentenceTokenizer
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle') # Loading PunktSentenceTokenizer using English pickle file
print(tokenizer.tokenize(text))

# %% Tokenize sentence of different language
spanish_tokenizer = nltk.data.load('tokenizers/punkt/PY3/spanish.pickle')
text = 'Hola amigo. Estoy bien.'
print(spanish_tokenizer.tokenize(text))

# %% Word Tokenization using work_tokenize
text = "Hello everyone. Welcome to GeeksforGeeks."
print(word_tokenize(text))

# %% Word Tokenization Using TreebankWordTokenizer 
tokenizer = TreebankWordTokenizer()
print(tokenizer.tokenize(text))

# %% Word Tokenization using WordPunctTokenizer
tokenizer = WordPunctTokenizer()
print(tokenizer.tokenize("Let's see how it's working."))

# %% Word Tokenization using Regular Expression 
tokenizer = RegexpTokenizer(r'\w+')
text = "Let's see how it's working."
print(tokenizer.tokenize(text))
# %%
