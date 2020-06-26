# author: Kerem Delikmen
# date: 26.06.2020
# desc: This function, show Toast Messages
from win10toast import ToastNotifier


def create_success_toast_message(success_title, success_text):
    ToastNotifier().show_toast(success_title, success_text, icon_path="../utils/toast-icons/success.ico")


def create_info_toast_message(info_title, info_text):
    ToastNotifier().show_toast(info_title, info_text, icon_path="../utils/toast-icons/info.ico.ico")


def create_error_toast_message(error_title, error_text):
    ToastNotifier().show_toast(error_title, error_text, icon_path="../utils/toast-icons/error.ico")