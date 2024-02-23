import telebot
from text_clasificacion import text_clasificacion
from text_horario import text_horario
from text_resultados import text_resultados
from text_infantiles import text_infantiles
from text_cuartos import text_cuartos

bot = telebot.TeleBot("6822504022:AAH2z4sNp4GJBRy8YHXmRCBvGnrQfbOlecs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Bot para mostrar informacion del Adepo Infantil A. Escribe /horario, /resultados, /clasificacion, /infantiles o /cuartos")

@bot.message_handler(commands=['horario','Horario'])
def echo_all(message):
  bot.reply_to(message, text_horario())

@bot.message_handler(commands=['clasificacion','Clasificacion'])
def echo_all(message):
  bot.reply_to(message, text_clasificacion())

@bot.message_handler(commands=['resultados','Resultados'])
def echo_all(message):
  bot.reply_to(message, text_resultados())

@bot.message_handler(commands=['infantiles','Infantiles'])
def echo_all(message):
  bot.reply_to(message, text_infantiles())

@bot.message_handler(commands=['cuartos','Cuartos'])
def echo_all(message):
  bot.reply_to(message, text_cuartos())

bot.infinity_polling()