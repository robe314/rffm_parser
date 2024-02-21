import telebot
from text_dict import text
from horarios import get_horarios
from text_clasificacion import text_clasificacion
from text_horario import text_horario

clasificacion=text_clasificacion()
horario=text_horario()

bot = telebot.TeleBot("6822504022:AAH2z4sNp4GJBRy8YHXmRCBvGnrQfbOlecs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Escribe /horario, /cuartos, /clasificacion")

@bot.message_handler(commands=['horario','Horario'])
def echo_all(message):
  bot.reply_to(message, horario)

@bot.message_handler(commands=['clasificacion','Clasificacion'])
def echo_all(message):
  bot.reply_to(message, clasificacion)

@bot.message_handler(commands=['cuartos','Cuartos'])
def echo_all(message):
  bot.reply_to(message, get_table())

bot.infinity_polling()