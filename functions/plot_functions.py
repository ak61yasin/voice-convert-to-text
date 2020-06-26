# Author: Kerem Delikmen
# Date: 26.06.2020
# Desc: This function, Understanding the distribution of the sequences
import matplotlib.pyplot as plt
import pandas as pd


def plot_cleaned_text_and_cleaned_summary_array(cleaned_text, cleaned_summary):
    text_word_count = []
    summary_word_count = []
    for i in cleaned_text:
        text_word_count.append(len(i.split()))

    for i in cleaned_summary:
        summary_word_count.append(len(i.split()))

    length_df = pd.DataFrame({'text': text_word_count, 'summary': summary_word_count})
    length_df.hist(bins=30)
    plt.show()