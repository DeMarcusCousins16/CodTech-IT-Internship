
# Generative Text Model - Python Script Version
# This script demonstrates text generation using GPT-2 (Transformers) and a basic LSTM (TensorFlow/Keras)

# Install required libraries if not already installed
# pip install transformers tensorflow

# GPT-2 Text Generation
from transformers import pipeline

print("Generating text with GPT-2:")
generator = pipeline('text-generation', model='gpt2')
prompt = "The future of AI in education is"
results = generator(prompt, max_length=100, num_return_sequences=1)
print("GPT-2 Output:")
print(results[0]['generated_text'])

# LSTM Text Generation Example
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

print("\nTraining LSTM model on a sample dataset:")
# Sample dataset
text = 'Deep learning allows computational models that are composed of multiple processing layers to learn representations of data with multiple levels of abstraction.'
chars = sorted(list(set(text)))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

# Sequence creation
maxlen = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])

X = np.zeros((len(sentences), maxlen, len(chars)), dtype=bool)
y = np.zeros((len(sentences), len(chars)), dtype=bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

# Define and compile the model
model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars))))
model.add(Dense(len(chars), activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Train the model (1 epoch for demo)
model.fit(X, y, batch_size=128, epochs=1)
