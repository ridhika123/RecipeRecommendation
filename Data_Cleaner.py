import unidecode
import ast
import nltk
from nltk.stem import WordNetLemmatizer
import pandas as pd
import re


def ingredient_cleaner(ingreds):
    lemmatizer = WordNetLemmatizer()
    words_to_remove = ["as", "required", "chopped", "medium", "fresh", "boiled", "peeled", "and", "finely", "a", "pinch",                    
                       "slice", "crushed", "fillet", "sliced", "few", "strand", "browned", "loaf", "piece", "into", "cube", 
                       "garnishing", "tablespo", "drop", "shaving", "drained", "grated", "gram", "soaked", "roughly", "blanched",
                        "scraped", "ice", "large", "halved", "washed", "seeded", "in", "deveined", "diced", "slivered", "shelled",
                       "quartered", "bulb", "overnight", "on", "pearl", "desiccated", "the", "at", "from", "cup", "one", "two", 
                       "three", "four", "five", "six", "seven", "eight", "nine", "ten", "plenty", "of", "", " "]
    
    if isinstance(ingreds, list):
        items = ingreds
    else:
        items = ast.literal_eval(ingreds)
       
    # converting all ingredients to unicode  
    items = [unidecode.unidecode(word) for word in items]
    
    # converting all ingredients to lower case
    items = [word.lower() for word in items]        
    
    # getting rid of all information beyond a comma
    items = [word.split(",")[0] for word in items]
    
    # deleting all punctuations
    items = [word.replace("(", "") for word in items]
    items = [word.replace(")", "") for word in items]
    items = [word.replace("/", " ") for word in items]
    items = [word.replace("-", " ") for word in items]
    items = [word.replace("+", " ") for word in items]
    items = [word.replace("?", " ") for word in items]
    
    # getting rid of all information beyond any number
    items = [re.split(r'(\d+)', word)[0] for word in items]
    
    # getting rid of any information beyond to, for, cut and with
    items = [word.split(" to")[0] for word in items]
    items = [word.split("for")[0] for word in items]
    items = [word.split("cut")[0] for word in items]
    items = [word.split(" with")[0] for word in items]
    
    # replace double spaces with single space
    items = [word.replace("  ", " ") for word in items]
                          
    # delete any ingredient which contains oil, salt, butter, sugar or lemon
    items = [word for word in items if word.find("oil") == -1]
    items = [word for word in items if word.find("salt") == -1]
    items = [word for word in items if word.find("butter") == -1]
    items = [word for word in items if word.find("sugar") == -1]
    items = [word for word in items if word.find("lemon") == -1]
    
    items_lemmatized = []
    for i in range(0, len(items)):
        to_lemma = items[i].split(' ')
        # lemmatizing words
        word_lemmatized = [lemmatizer.lemmatize(word) for word in to_lemma]
        # removing words in words_to_remove
        word_cleaned = ' '.join([word for word in word_lemmatized if word not in words_to_remove])
        items_lemmatized.append(word_cleaned.lstrip().rstrip())
    items_lemmatized = [word for word in items_lemmatized if word != '']
    
    return items_lemmatized   