import telebot
from text_clasificacion import text_clasificacion
from text_horario import text_horario
from text_resultados import text_resultados
from text_infantiles import text_infantiles
from text_cuartos import text_cuartos

clasificacion=text_clasificacion()
horario=text_horario()
resultados=text_resultados()
infantiles=text_infantiles()
cuartos=text_cuartos()

bot = telebot.TeleBot("6822504022:AAH2z4sNp4GJBRy8YHXmRCBvGnrQfbOlecs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Escribe /horario, /resultados, /clasificacion, /infantiles o /cuartos")

@bot.message_handler(commands=['horario','Horario'])
def echo_all(message):
  bot.reply_to(message, horario)

@bot.message_handler(commands=['clasificacion','Clasificacion'])
def echo_all(message):
  bot.reply_to(message, clasificacion)

@bot.message_handler(commands=['resultados','Resultados'])
def echo_all(message):
  bot.reply_to(message, resultados)

@bot.message_handler(commands=['infantiles','Infantiles'])
def echo_all(message):
  bot.reply_to(message, infantiles)

@bot.message_handler(commands=['cuartos','Cuartos'])
def echo_all(message):
  bot.reply_to(message, cuartos)

bot.infinity_polling()