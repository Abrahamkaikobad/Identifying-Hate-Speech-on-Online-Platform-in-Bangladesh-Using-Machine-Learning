import re
import string
from bltk.langtools import Tokenizer
from nltk.tokenize import word_tokenize
# Bangla package import
from bltk.langtools import remove_stopwords
from bltk.langtools import Tokenizer
from bltk.langtools.banglachars import (vowels, vowel_signs, consonants, digits, operators, punctuations, others)

# Other imports...

tokenizer = Tokenizer()
# Function to clean Bangla text
def clean_bangla_text(text):
    tokened_words = tokenizer.word_tokenizer(text)
    remove_stop = remove_stopwords(tokened_words, level='hard')
    remove_punc = [word for word in remove_stop if word not in punctuations]
    remove_digit = [word for word in remove_punc if word not in digits]
    cleaned_text = ' '.join(remove_digit)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

def clean_banglish_text(text):
    text = re.sub(f"[{string.punctuation}{string.digits}]", "", text)
    with open('src/data/banglish_stop.txt', 'r', encoding='utf-8') as file:
        ignored_words = set(word.strip() for word in file.readlines())
    tokens = tokenizer.word_tokenizer(text)
    processed_text = [token.lower() for token in tokens if token not in ignored_words]
    return ' '.join(processed_text)

# # Sample Bangla text
# bangla_text = "তুই কি মাগির পুত?"

# # Sample Banglish text
# banglish_text = "tui ki magir put?."

# # Clean Bangla text
# cleaned_bangla = clean_bangla_text(bangla_text)
# print("Cleaned Bangla Text:", cleaned_bangla)

# # Clean Banglish text
# cleaned_banglish = clean_banglish_text(banglish_text)
# print("Cleaned Banglish Text:", cleaned_banglish)
