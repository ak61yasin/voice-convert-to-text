# Author: Kerem Delikmen
# Date: 26.06.2020
# Desc: This function, define nlp functions
import re

from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from bs4 import BeautifulSoup


def text_cleaner(text, contraction_mapping):
    stop_words = set(stopwords.words('english'))
    newString = text.lower()
    newString = BeautifulSoup(newString, "lxml").text
    newString = re.sub(r'\([^)]*\)', '', newString)
    newString = re.sub('"','', newString)
    newString = ' '.join([contraction_mapping[t] if t in contraction_mapping else t for t in newString.split(" ")])
    newString = re.sub(r"'s\b","",newString)
    newString = re.sub("[^a-zA-Z]", " ", newString)
    tokens = [w for w in newString.split() if not w in stop_words]
    long_words=[]
    for i in tokens:
        if len(i)>=3:
            long_words.append(i)
    return (" ".join(long_words)).strip()


def summary_cleaner(text, contraction_mapping):
    newString = re.sub('"','', text)
    newString = ' '.join([contraction_mapping[t] if t in contraction_mapping else t for t in newString.split(" ")])
    newString = re.sub(r"'s\b","",newString)
    newString = re.sub("[^a-zA-Z]", " ", newString)
    newString = newString.lower()
    tokens=newString.split()
    newString=''
    for i in tokens:
        if len(i)>1:
            newString=newString+i+' '
    return newString


def text_tokenizer(x_tr, x_val, max_len_text):
    x_tokenizer = Tokenizer()
    x_tokenizer.fit_on_texts(list(x_tr))

    # convert text sequences into integer sequences
    x_tr = x_tokenizer.texts_to_sequences(x_tr)
    x_val = x_tokenizer.texts_to_sequences(x_val)

    # padding zero upto maximum length
    x_tr = pad_sequences(x_tr, maxlen=max_len_text, padding='post')
    x_val = pad_sequences(x_val, maxlen=max_len_text, padding='post')

    x_voc_size = len(x_tokenizer.word_index) + 1
    return x_voc_size


def summary_tokenizer(y_tr, y_val, max_len_summary):
    y_tokenizer = Tokenizer()
    y_tokenizer.fit_on_texts(list(y_tr))

    # convert summary sequences into integer sequences
    y_tr = y_tokenizer.texts_to_sequences(y_tr)
    y_val = y_tokenizer.texts_to_sequences(y_val)

    # padding zero upto maximum length
    y_tr = pad_sequences(y_tr, maxlen=max_len_summary, padding='post')
    y_val = pad_sequences(y_val, maxlen=max_len_summary, padding='post')

    y_voc_size = len(y_tokenizer.word_index) + 1
    return y_voc_size