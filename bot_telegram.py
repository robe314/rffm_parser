import telebot
from text_dict import text
from horarios import get_horarios

myurl = "https://www.rffm.es/competicion/calendario?temporada=19&tipojuego=1&competicion=17145553&grupo=17145567"
horario=text(get_horarios(myurl))

bot = telebot.TeleBot("6822504022:AAH2z4sNp4GJBRy8YHXmRCBvGnrQfbOlecs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Escribe /horario o /cuartos")

@bot.message_handler(commands=['horario','Horario'])
def echo_all(message):
  bot.reply_to(message, horario)

@bot.message_handler(commands=['cuartos','Cuartos'])
def echo_all(message):
  bot.reply_to(message, get_table())

bot.infinity_polling()