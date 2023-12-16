import json
from gensim.utils import simple_preprocess
import re
from pathlib import Path
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def preprocess_and_tokenize_with_stopwords(item):
    stop_words = set(stopwords.words('english'))
    if isinstance(item, str):
        # If the item is a string, preprocess, tokenize, and remove stop words
        tokens = simple_preprocess(re.sub(r'\W', ' ', item.lower()))
        return [word for word in tokens if word not in stop_words]
    elif isinstance(item, dict):
        # If the item is a dictionary, recursively preprocess and tokenize its values
        return [preprocess_and_tokenize_with_stopwords(value) for value in item.values()]
    else:
        # If the item is neither a string nor a dictionary, return an empty list
        return []

# Function to find and store paragraphs with stop words removed
def find_and_store_paragraphs_with_stopwords(data, paragraphs_list):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "paragraphs":
                # Found "paragraphs" attribute, extract contents and preprocess with stop words removal
                paragraphs_list.extend(preprocess_and_tokenize_with_stopwords(value))
            else:
                find_and_store_paragraphs_with_stopwords(value, paragraphs_list)
    elif isinstance(data, list):
        for item in data:
            find_and_store_paragraphs_with_stopwords(item, paragraphs_list)

# List to store extracted and preprocessed paragraphs
extracted_paragraphs = []

# Call the function to find and store "paragraphs" after preprocessing

directory = Path('./json_formatted_files')  
new_output_list = []
# Iterate through files in the directory
for item in directory.iterdir():
    if item.is_file():
        with open(f'/home/siddy/Desktop/lawProject/json_formatted_files/{item.name}', 'r') as file:
            json_data = json.load(file)
            find_and_store_paragraphs_with_stopwords(json_data, extracted_paragraphs)


with open('check.txt', 'w') as file:
    for item in extracted_paragraphs:
        flat_list = flatten_list(item)
        if len(flat_list) > 0:
            new_output_list.append(flat_list)
        file.write(f"""{flat_list}\n""")
