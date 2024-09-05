from django.core.management.base import BaseCommand
from django.conf import settings

import telebot
from bot.keyboards import get_languages, user_types, get_registration
from bot.utils import default_languages, introduction_template
from bot.states import LegalRegisterState, IndividualRegisterState
BOT_TOKEN = settings.BOT_TOKEN

bot = telebot.TeleBot(token=BOT_TOKEN)

user_languages = {}

all_languages = ['uz', 'ru']

@bot.message_handler(commands=['start'])
def welcome(message):
    lang_uz = default_languages['uz']
    lang_ru = default_languages['ru']
    text = (f"{lang_uz['welcome_message']}\n"
            f"{lang_uz['choose_language']}\n\n"
            f"{lang_ru['welcome_message']}\n"
            f"{lang_ru['choose_language']}\n")

    bot.send_message(chat_id=message.chat.id, text=text, reply_markup=get_languages())


@bot.callback_query_handler(func=lambda call: call.data == 'registration')
def registration(call):
    lang = user_languages[call.from_user.id]
    text = "Foydalanuvchi turini tanlang"
    bot.send_message(chat_id=call.from_user.id, text=text, reply_markup=user_types(lang))


@bot.callback_query_handler(func=lambda call: call.data.split("_")[0] == 'lang')
def select_language(call):
    print("call back data", call)
    user_id = call.from_user.id
    print("user id:", user_id)
    lang = call.data.split("_")[1]
    if lang in all_languages:
        user_languages[user_id] = call.data.split("_")[1]
        bot.send_message(chat_id=call.from_user.id, text=introduction_template, reply_markup=get_registration(lang))
    else:
        bot.send_message(chat_id=user_id, text="You are not choose right language")




@bot.callback_query_handler(lambda call: call.data in ['legal', 'individual'])
def legal_registration(call):
    if call.data == 'legal':
        bot.send_message(chat_id=call.message.chat_id, text="Kompaniya nomini kiriting")
        bot.set_state(user_id=call.message.chat.id, state=LegalRegisterState.COMPANY_NAME)
    elif call.data == 'individual':
        bot.send_message(chat_id=call.message.chat_id, text="To'liq ismingizni kiriting")
        bot.set_state(user_id=call.message.chat.id, state=IndividualRegisterState.NAME)








class Command(BaseCommand):

    def handle(self, *args, **options):
        bot.infinity_polling()