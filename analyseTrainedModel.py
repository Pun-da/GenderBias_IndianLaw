from gensim.models import KeyedVectors
import sys

# Load the Word2Vec model from the .bin file
model_path = './trainingData/legalModel_noStem.bin'  # Replace with your file path
word_vectors = KeyedVectors.load_word2vec_format(model_path, binary=True)

# for index, word in enumerate(word_vectors.index_to_key):
#     if index == 20 : 
#         break;
#     embedding = word_vectors[word]
#     print(f"Key: {index}, Word: {word}, Embedding: {embedding}")


# sys.exit()

# Get the word vector for a specific word
# word = 'court'
# if word in word_vectors:
#     print(f"Vector for '{word}':\n{word_vectors[word]}")
# else:
#     print(f"'{word}' is not in the vocabulary.")


# Find similar words
similar_words = word_vectors.most_similar('divorced', topn=100)

print("Most similar words:\n\n")

for word in similar_words : 
    print(word)


sys.exit();

# Perform vector arithmetic (e.g., king - man + woman)
result = word_vectors.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
print(f"\nResult of 'king - man + woman':\n{result}")






