import re

# Uses three space as paragraph delimiter to convert the text into list of paragraphs.
def create_paragraphs_list(string):
  paragraphs_list = re.split('\s{3,}', string);
  return paragraphs_list

def remove_break_lines_from_list(string_list):
  transformed_list = [string.replace('\n', '') for string in string_list]
  return transformed_list

def remove_blacklist_words(string_list, blacklist):
    filtered_list = []
    for string in string_list:
        if not any(word in string for word in blacklist):
            filtered_list.append(string)
    return filtered_list

def remove_empty_strings(string_list):
    return [s for s in string_list if s]
    

def transform_text(string, blacklist):
    paragraphs_list = create_paragraphs_list(string)
    transformed_list = remove_break_lines_from_list(paragraphs_list)
    transformed_list = remove_blacklist_words(transformed_list, blacklist)
    transformed_list = remove_empty_strings(transformed_list)        
    return ' '.join(transformed_list)