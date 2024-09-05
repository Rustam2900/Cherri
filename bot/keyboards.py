from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.utils import default_languages

def get_languages():
    lang = InlineKeyboardMarkup()
    lang_uz = InlineKeyboardButton(text="uz 🇺🇿", callback_data="lang_uz")
    lang_ru = InlineKeyboardButton(text="ru 🇷🇺", callback_data="lang_ru")

    lang.add(lang_uz, lang_ru)
    return lang


def user_types(lang):
    person = InlineKeyboardMarkup()
    individual = InlineKeyboardButton(text=default_languages[lang]['individual'], callback_data="individual")
    legal = InlineKeyboardButton(text=default_languages[lang]["legal"], callback_data="legal")
    person.add(individual, legal)
    return person

def get_registration(lang):
    reg = InlineKeyboardMarkup()
    reg_btn = InlineKeyboardButton(text=default_languages[lang]['registration'], callback_data="registration")
    reg.add(reg_btn)
    return reg