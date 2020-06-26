from functions import const_functions, nlp_functions,read_and_write_file_functions
import pandas as pd
import numpy as np

# Read a text
data = pd.read_csv("../utils/dataset/reviews.csv")

# Get contraction map list
contraction_map = const_functions.get_contraction_map()

# Created cleared text
cleaned_text = []
for i in data['Text']:
    cleaned_text.append(nlp_functions.nlp_text_cleaner(i, contraction_map))

print(cleaned_text)
