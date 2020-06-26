# author: Kerem Delikmen
# date: 26.06.2020
# desc: This function, make I/O operations
import speech_recognition as sr
from functions import log_messages_functions


# speech_recognition_instance: Create a Recognizer instance
def speech_recognition_instance():
    log_messages_functions.info_log_message("speech_recognition_instance function: Create a Recognizer instance")
    return sr.Recognizer()


# read_voice_file: Retrieves the source video file
# Params: voice_path: source file path.
def read_voice_file(voice_path):
    log_messages_functions.info_log_message("read_voice_file function: Create a AudioFile ")
    return sr.AudioFile(voice_path)


# voice_to_text: Converts voice(voice file) to text
def voice_to_text(voice_file, lang='tr'):

    with voice_file as source_file:
        try:
            speech_recognition_instance().adjust_for_ambient_noise(source_file)
            audio_file = speech_recognition_instance().record(source_file)
            result = speech_recognition_instance().recognize_google(audio_file, language=lang)
            log_messages_functions.success_log_message("voice_to_text functions: Convert voice to text")
            log_messages_functions.success_log_message("voice_to_text functions: Success Text: " + result)
        except Exception as e:
            log_messages_functions.error_log_message("voice_to_text functions: Voice not convert to text")
            log_messages_functions.error_log_message("voice_to_text functions: Error Message:  " + str(e))
            return e

    return result
