# %% Building a Simple Neural Network with an Embedding Layer
import tensorflow as tf
from tensorflow.keras import layers, models

vocab_size = 10000  # Size of the vocabulary 
embedding_dim = 128  # Dimension of the embedding vector
input_length = 100  # Length of input sequences

model = models.Sequential()
# Embedding layer
# input_dim refers to the size of the vocabulary, which is the number of unique words.
# output_dim specifies the size of each word's vector, also known as the embedding size. For example, each word could be represented as a 128-dimensional vector.
# input_length defines the length of each input sequence.
model.add(layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=input_length))
model.add(layers.GlobalAveragePooling1D())  
model.add(layers.Dense(64, activation='relu'))  
model.add(layers.Dense(1, activation='sigmoid')) 
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Check the model summary
model.build(input_shape=(None, input_length)) 
model.summary()

# In the model summary, embedding layers an output shape of (None, 100, 128), 
# meaning it processes input sequences of length 100 and maps each token to a 128-dimensional vector. 
# The layer contains 1,280,000 parameters, which are the embeddings for each word in the vocabulary. 
# These parameters will be learned during training.