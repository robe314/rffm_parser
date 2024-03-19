import telebot
from variables import *
from dict2png import dict2png
from dict_clasificacion import dict_clasificacion
from dict_horarios import dict_horarios
from dict_cuartos import dict_cuartos
from dict_infantiles import dict_infantiles
from dict_resultados import dict_resultados

bot = telebot.TeleBot("6822504022:AAH2z4sNp4GJBRy8YHXmRCBvGnrQfbOlecs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Bot para mostrar informacion del Adepo Infantil A. Escribe /horario, /resultados, /clasificacion, /infantiles o /cuartos")

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
  dict2png(dict_resultados(url_calendario))
  photo = open('borrar.png', 'rb')
  bot.send_photo(13336098,photo)

@bot.message_handler(commands=['infantiles','Infantiles'])
def echo_all(message):
  dict2png(dict_infantiles(url_seguidos))
  photo = open('borrar.png', 'rb')
  bot.send_photo(13336098,photo)

@bot.message_handler(commands=['cuartos','Cuartos'])
def echo_all(message):
  dict2png(dict_cuartos(url_cuartos))
  photo = open('borrar.png', 'rb')
  bot.send_photo(13336098,photo)

bot.infinity_polling()