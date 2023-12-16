from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
import os, sys

sys.path.append('..')  

from jsonExtractTest import new_output_list 
data = new_output_list


# sys.exit();

# Train Word2Vec legal_model
legal_model = Word2Vec(sentences=data, vector_size=100, window=5, min_count=1, workers=4)

# Save the legal_model
legal_model.save('word2vec_model.model')
legal_model.wv.save_word2vec_format("legalModel_noStem.bin", binary=True)

for index, word in enumerate(legal_model.wv.index_to_key):
    if index == 10:
        break
    print(f"word #{index}/{len(legal_model.wv.index_to_key)} is {word}")


print(legal_model.wv.vectors.shape)



# most_sim = legal_model.wv.most_similar(positive=['university'], negative=[], topn=5)
# print(most_sim)

# for word in legal_model.wv.index_to_key : 
#     print(word)


