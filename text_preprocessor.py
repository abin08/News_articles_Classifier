import pandas as pd
import numpy as np
import spacy
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from bs4 import BeautifulSoup
import re
import unicodedata

sp = spacy.load('en', parse=True, tag=True, entity=True)
tokenizer = ToktokTokenizer()
stopwords_list = nltk.corpus.stopwords.words('english')

def remove_html_tags(text):
    """
    Removes html tags from text using BeautifulSoup
    """
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text()
    return stripped_text

def remove_accented_chars(text):
    """
    Converts accented characters to standard ASCII characters
    eg: Áccěntěd těxt is converted as Accented text
    """
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

def remove_special_chars(text, remove_digits=False):
    """
    Removes special characters from text using regular expression, also
    removes digits if remove_digits is True
    """
    pattern = r'[^a-zA-Z0-9\s]' if not remove_digits else r'[^a-zA-Z\s]'
    text = re.sub(pattern, '', text)
    return text

def get_stem(text):
    """
    Performs stemming on the words of text using nltk PorterStemmer
    """
    ps = nltk.PorterStemmer()
    text = ' '.join([ps.stem(word) for word in text.split()])
    return text

def lemmatize_text(text):
    """
    Lemmatize the words using spacy
    Note: Pronouns are excluded (eg: he, she, my, it etc...)
    """
    text = sp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text

def remove_stopwords(text):
    """
    Removes stopwords from the text using nltk stopwords_list
    """
    tokens = get_tokens(text)
    filtered_tokens = [token for token in tokens if token not in stopwords_list]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text

def get_tokens(text):
    """
    Converts text to a list of tokens using nltk tokenizer
    """
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    return tokens

# def clean_text(doc, html_tag_removal=True, accented_chars_removal=True, 
#     special_chars_removal=True, stemming=True, 
#     lemmatization=True, stopwords_removal=True, remove_digits=True):
#     """
#     Performs text preprocessing methods on the text based on true arguments
#     """
#     if html_tag_removal:
#         doc = remove_html_tags(doc)
#     if accented_chars_removal:
#         doc = remove_accented_chars(doc)
#     if special_chars_removal:
#         doc = remove_special_chars(doc, remove_digits=remove_digits)
#     # if stemming:
#         # doc = get_stem(doc)
#     if lemmatization:
#         doc = lemmatize_text(doc)
#     if stopwords_removal:
#         doc = remove_stopwords(doc)
#     return doc