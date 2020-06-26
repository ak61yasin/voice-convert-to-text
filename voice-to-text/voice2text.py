# author: Kerem Delikmen
# date: 26.06.2020
# desc: This function, convert Voice(Voice File) to text
from functions import const_functions, voice_operations_functions, toast_messages_functions, log_messages_functions


VOICE_FILE_PATH = const_functions.get_video_path("voice2.wav")

voice_file = voice_operations_functions.read_voice_file(VOICE_FILE_PATH)
result = voice_operations_functions.voice_to_text(voice_file)

file = read_and_write_file_functions.open_file()

if result != " ":
    toast_messages_functions.create_success_toast_message("Success", "Voice Convert To Text")
    read_and_write_file_functions.write_file(file, result)
    print(result)
    log_messages_functions.success_log_message("voice2text.py file: Transformed Text Shown")
else:
    toast_messages_functions.create_error_toast_message("Error", "Voice Not Convert To Text")
    log_messages_functions.error_log_message("Voice Not Convert To Text -> Error Message: " + result)
