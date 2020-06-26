import pandas as pd
import numpy as np
import warnings

from attention import AttentionLayer
from functions import nlp_functions, const_functions, plot_functions
from keras import backend as K
from attention import AttentionLayer
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Input, LSTM, Embedding, Dense, Concatenate, TimeDistributed, Bidirectional
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping

# Read a text.
data = pd.read_csv("../utils/dataset/Reviews.csv", nrows=10000)

# returns only the dataframe’s unique values. Removing duplicate records is sample.
data.drop_duplicates(subset=['Text'], inplace=True)

# remove missing values.
data.dropna(axis=0, inplace=True)

# get contraction_mapping
contraction_mapping = const_functions.get_contraction_map()

cleaned_text = []
for t in data['Text']:
    cleaned_text.append(nlp_functions.text_cleaner(t, contraction_mapping))

cleaned_summary = []
for t in data['Summary']:
    cleaned_summary.append(nlp_functions.summary_cleaner(t, contraction_mapping))

data['cleaned_text'] = cleaned_text
data['cleaned_summary'] = cleaned_summary
data['cleaned_summary'].replace('', np.nan, inplace=True)
data.dropna(axis=0, inplace=True)

data['cleaned_summary'] = data['cleaned_summary'].apply(lambda x : '_START_ '+ x + ' _END_')

for i in range(5):
    print("Review:", data['cleaned_text'][i])
    print("Summary:", data['cleaned_summary'][i])
    print("\n")

plot_functions.plot_cleaned_text_and_cleaned_summary_array(data['cleaned_text'], data['cleaned_summary'])

# %90 train, %10 validation
x_train, x_valid, y_train, y_valid = train_test_split(data['cleaned_text'], data['cleaned_summary'],
                                                      test_size=0.1, random_state=0, shuffle=True)

# Tokenizer Operations
# Text tokenizer
x_voc_size = nlp_functions.text_tokenizer(x_train, x_valid, const_functions.get_max_len_text())

# Summary Tokenizer
y_voc_size = nlp_functions.summary_tokenizer(y_train, y_valid, const_functions.get_max_len_summary())

# Model Building

K.clear_session()
latent_dim = 500

# Encoder
encoder_inputs = Input(shape=(const_functions.get_max_len_text(),))
enc_emb = Embedding(x_voc_size, latent_dim,trainable=True)(encoder_inputs)

#LSTM 1
encoder_lstm1 = LSTM(latent_dim,return_sequences=True,return_state=True)
encoder_output1, state_h1, state_c1 = encoder_lstm1(enc_emb)

#LSTM 2
encoder_lstm2 = LSTM(latent_dim,return_sequences=True,return_state=True)
encoder_output2, state_h2, state_c2 = encoder_lstm2(encoder_output1)

#LSTM 3
encoder_lstm3=LSTM(latent_dim, return_state=True, return_sequences=True)
encoder_outputs, state_h, state_c= encoder_lstm3(encoder_output2)

# Set up the decoder.
decoder_inputs = Input(shape=(None,))
dec_emb_layer = Embedding(y_voc_size, latent_dim,trainable=True)
dec_emb = dec_emb_layer(decoder_inputs)

#LSTM using encoder_states as initial state
decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_outputs,decoder_fwd_state, decoder_back_state = decoder_lstm(dec_emb,initial_state=[state_h, state_c])

#Attention Layer
attn_layer = AttentionLayer(name='attention_layer')
attn_out, attn_states = attn_layer([encoder_outputs, decoder_outputs])

# Concat attention output and decoder LSTM output
decoder_concat_input = Concatenate(axis=-1, name='concat_layer')([decoder_outputs, attn_out])

#Dense layer
decoder_dense = TimeDistributed(Dense(y_voc_size, activation='softmax'))
decoder_outputs = decoder_dense(decoder_concat_input)

# Define the model
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
model.summary()

model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy')

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1)

# TODO: model fit.