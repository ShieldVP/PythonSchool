import telebot
from telebot import types


TOKEN = ''
bot = telebot.TeleBot(TOKEN)


class User:
    name = None
    surname = None


users = []


@bot.message_handler(commands=["reg"])
def reg(message):
    bot.send_message(message.from_user.id, "Как тебя зовут?")
    users.append(User())
    bot.register_next_step_handler(message, get_name)


@bot.message_handler(func=lambda mes: 'Сколько' in mes.text)
def get_num_users(message):
    bot.send_message(message.from_user.id, str(len(users)))


def get_name(message):
    global users
    name = message.text
    users[-1].name = name
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global users
    user = users[-1]
    surname = message.text
    user.surname = surname

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_yes)
    keyboard.add(key_no)
    question = 'Ты ' + user.name + '  ' + user.surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(callback):
    if callback.data == "yes":
        bot.send_message(callback.message.chat.id, 'Записал')
    elif callback.data == "no":
        global users
        users.pop()
        bot.send_message(callback.message.chat.id, 'Попробуйте пройти регистрацию снова /reg')


bot.infinity_polling()
