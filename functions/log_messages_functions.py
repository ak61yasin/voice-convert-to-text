import datetime


def error_log_message(text):
    open("../utils/logs/error/error_log.txt", "a", encoding="utf-8").write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + " -> " + text + " \n")


def info_log_message(text):
    open("../utils/logs/info/info_log.txt", "a", encoding="utf-8").write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + " -> " + text + " \n")


def success_log_message(text):
    open("../utils/logs/success/success_log.txt", "a", encoding="utf-8").write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + " -> " + text + " \n")