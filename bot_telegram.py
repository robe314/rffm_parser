import telebot
from variables import *
from dict2text import dict2text
from dict_clasificacion import dict_clasificacion
from dict_horarios import dict_horarios
from dict_resultados import dict_resultados
from dict_seguidos import dict_seguidos
from dict_coeficiente import dict_coeficiente

bot = telebot.TeleBot("6822504022:AAH2z4sNp4GJBRy8YHXmRCBvGnrQfbOlecs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Bot para mostrar informacion del Adepo Cadete B. Escribe /horario, /resultados, /clasificacion, /seguidos o /coeficientes")

@bot.message_handler(commands=['horario','Horario'])
def echo_all(message):
  bot.reply_to(message, dict2text(dict_horarios(url_calendario)))

@bot.message_handler(commands=['clasificacion','Clasificacion'])
def echo_all(message):
  bot.reply_to(message, dict2text(dict_clasificacion(url_clasificacion)))

@bot.message_handler(commands=['resultados','Resultados'])
def echo_all(message):
  bot.reply_to(message, dict2text(dict_resultados(url_resultados)))

@bot.message_handler(commands=['seguidos','Seguidos'])
def echo_all(message):
  bot.reply_to(message, dict2text(dict_seguidos(url_seguidos)))

@bot.message_handler(commands=['coeficiente','Coeficiente'])
def echo_all(message):
  bot.reply_to(message, dict2text(dict_coeficiente(url_coeficiente,puesto)))

bot.infinity_polling()