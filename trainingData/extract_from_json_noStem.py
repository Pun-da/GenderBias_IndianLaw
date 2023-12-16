import json
from gensim.utils import simple_preprocess
import re

# Load JSON data from a file
with open("./json_formatted_files/A2020_32.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Define a function to preprocess and tokenize text
def preprocess_and_tokenize(item):
    if isinstance(item, str):
        # If the item is a string, preprocess and tokenize it
        return simple_preprocess(re.sub(r'\W', ' ', item.lower()))
    elif isinstance(item, dict):
        # If the item is a dictionary, recursively preprocess and tokenize its values
        return [preprocess_and_tokenize(value) for value in item.values()]
    else:
        # If the item is neither a string nor a dictionary, return an empty list
        return []

output_list = []

# Iterate over chapters
for chapter_id, chapter_info in data["Chapters"].items():
    chapter_name = chapter_info["Name"]

    # Iterate over sections
    for section_id, section_info in chapter_info["Sections"].items():
        section_heading = section_info["heading"]

        # Iterate over paragraphs
        for paragraph_id, paragraph_text in section_info["paragraphs"].items():
            # Extract text from each paragraph
            text_list = preprocess_and_tokenize(paragraph_text)
            
            # Append the text list to the output list
            output_list.append({
                "Chapter": chapter_name,
                "Section": section_heading,
                "Paragraph": text_list
            })

# Print the output

# for item in output_list : 
#     print(item)
#     print("----")


def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

new_output_list = []

with open('nostem_sample_processed_json_output.txt', 'w') as file :
    for item in output_list : 
        flat_list = flatten_list(item['Paragraph'])
        new_output_list.append(flat_list)
        file.write(f"""{flat_list}\n""")