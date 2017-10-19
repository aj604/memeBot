import logging
import telebot
from time import sleep




token = "464830208:AAEw5n-hd2qaOUpys7Y5TSSOR8xIewwqP7Y"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Heyyy uhhh.... any questions?")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Soooo  you should probably start soon... but if not I'll just give you an extension")

@bot.message_handler(commands=['info'])
def get_info(message):
    bot.reply_to(message, "I am but a simple memer")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(func=lambda message: True)
def respond_to_question(message):
    bot.send_sticker(chat_id=message.id, data="hello")

def listener(messages):
    for m in messages:
        m

bot.set_update_listener(listener)
bot.polling()