# Author: Kerem Delikmne
# Date: 25.06.2020
# Desc: This function, writes text to the text.txt file
from functions import log_messages_functions


# open_file: Open text.txt file
def open_file():
    log_messages_functions.info_log_message("open_file function: Open text.txt file")
    return open("../utils/dataset/text.txt", "a", encoding="utf-8")


# write_file: Writes text.txt file
def write_file(file_name, text):
    log_messages_functions.info_log_message("write_file function: Writes text to text.txt file")
    log_messages_functions.info_log_message("Text: " + text)
    file_name.write(text)

    
# read_file: Return the text file in text.txt
def read_file():
    with open("../utils/dataset/text.txt", encoding="utf-8") as file:
        return file.readlines()
