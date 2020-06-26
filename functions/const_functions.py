# author: Kerem Delikmen
# date: 25.06.2020
# desc: This function, define const variables
from functions import log_messages_functions


def get_video_path(file_name):
    log_messages_functions.info_log_message("get_video_path function: Audio file path received ")
    return "../utils/source-file/"+file_name