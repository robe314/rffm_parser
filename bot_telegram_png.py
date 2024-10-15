import telebot
from variables import *
from dict2png import dict2png
from dict_clasificacion import dict_clasificacion
from dict_horarios import dict_horarios
from dict_coeficiente import dict_coeficiente
from dict_seguidos import dict_seguidos
from dict_resultados import dict_resultados
from dict_calendario import dict_calendario

bot = telebot.TeleBot("6822504022:AAH2z4sNp4GJBRy8YHXmRCBvGnrQfbOlecs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Bot para mostrar informacion del Adepo Infantil A. Escribe /horario, /resultados, /clasificacion, /calendario, /seguidos o /coeficiente")

@bot.message_handler(commands=['horario','Horario'])
def echo_all(message):
  dict2png(dict_horarios(url_calendario))
  photo = open('borrar.png', 'rb')
  bot.send_photo(13336098,photo)

@bot.message_handler(commands=['clasificacion','Clasificacion'])
def echo_all(message):
  dict2png(dict_clasificacion(url_clasificacion))
  photo = open('borrar.png', 'rb')
  bot.send_photo(13336098,photo)

@bot.message_handler(commands=['resultados','Resultados'])
def echo_all(message):
  dict2png(dict_resultados(url_resultados))
  photo = open('borrar.png', 'rb')
  bot.send_photo(13336098,photo)

@bot.message_handler(commands=['seguidos','Seguidos'])
def echo_all(message):
  dict2png(dict_seguidos(url_seguidos))
  photo = open('borrar.png', 'rb')
  bot.send_photo(13336098,photo)

@bot.message_handler(commands=['coeficiente','Coeficiente'])
def echo_all(message):
  dict2png(dict_coeficiente(url_coeficiente, puesto))
  photo = open('borrar.png', 'rb')
  bot.send_photo(13336098,photo)

@bot.message_handler(commands=['calendario','Calendario'])
def echo_all(message):
  dict2png(dict_calendario(url_calendario))
  photo = open('borrar.png', 'rb')
  bot.send_photo(13336098,photo)

bot.infinity_polling()