# Tokenization

Tokenization divides a Textual input into smaller units known as tokens.
These tokens can be in the form of words, characters, sub-words or sentences called tokens (chunks of informations).
It helps in improving interpretability of text by different models.

## Types of Tokenization

### Word Tokenization

Word tokenization is the most commonly used method where text is divided into individual words. It works well for languages with clear word boundaries, like English. For example, "Machine learning is fascinating" becomes:

- Input before tokenization: ["Machine Learning is fascinating"]
- Output when tokenized by words: ["Machine", "learning", "is", "fascinating"]

### Character Tokenization

In Character Tokenization, the textual data is split and converted to a sequence of individual characters. This is beneficial for tasks that require a detailed analysis, such as spelling correction or for tasks with unclear boundaries. It can also be useful for modelling character-level language.

- Input before tokenization: ["You are helpful"]
- Output when tokenized by characters: ["Y", "o", "u", " ", "a", "r", "e", " ", "h", "e", "l", "p", "f", "u", "l"]

### Sub-word Tokenization

This strikes a balance between word and character tokenization by breaking down text into units that are larger than a single character but smaller than a full word. This is useful when dealing with morphologically rich languages or rare words.

- ["Time", "table"]
- ["Rain", "coat"]
- ["Grace", "fully"]
- ["Run", "way"]

Sub-word tokenization helps to handle out-of-vocabulary words in NLP tasks and for languages that form words by combining smaller units.

### Sentence Tokenization

Sentence tokenization is also a common technique used to make a division of paragraphs or large set of sentences into separated sentences as tokens. This is useful for tasks requiring individual sentence analysis or processing.

- Input before tokenization: ["Artificial Intelligence is an emerging technology. Machine learning is fascinating. Computer Vision handles images. "]
- Output when tokenized by sentences ["Artificial Intelligence is an emerging technology.", "Machine learning is fascinating.", "Computer Vision handles images."]

### N-gram Tokenization

N-gram tokenization splits words into fixed-sized chunks (size = n) of data.

- Input before tokenization: ["Machine learning is powerful"]
- Output when tokenized by bigrams: [('Machine', 'learning'), ('learning', 'is'), ('is', 'powerful')]
