import pickle
import pandas as pd

import text_preprocessor as tp

with open('pickles/mnb_classifier.pickle','rb') as data:
    mnb_model = pickle.load(data)

with open('pickles/tfidf.pickle','rb') as data:
    tfidf = pickle.load(data)

category_codes = {
    'business':0,
    'entertainment':1,
    'sport':2,
    'politics':3,
    'tech':4
}

def category_name(category_id):
    for category, id_ in category_codes.items():
        if(id_ == category_id):
            return category

def predict_category(text):
    text = tp.clean_text(text)
    cat = mnb_model.predict(tfidf.transform([text]))
    return category_name(cat[0])

