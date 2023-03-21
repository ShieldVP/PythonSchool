import telebot
from telebot import types
from telebot.formatting import hitalic


TOKEN = ''
bot = telebot.TeleBot(TOKEN)
gonna_cry = 'https://media.tenor.com/VQ2Zec1wwIUAAAAC/spider-man-gonna-cry.gif'


@bot.message_handler(content_types=["text"])
def bully_echo(message):
    bot.send_message(message.chat.id, hitalic(message.text), parse_mode='HTML')
    if message.text == "Ну хватит":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Ну да, ну да")
        item2 = types.KeyboardButton("Ладно...")
        markup.add(item1)
        markup.add(item2)

        bot.send_video(
            message.chat.id,
            gonna_cry,
            caption='No',
            reply_to_message_id=message.id,
            reply_markup=markup
        )


bot.infinity_polling()
