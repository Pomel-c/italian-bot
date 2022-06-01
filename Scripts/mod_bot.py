# ./venv/Scripts/Activate.ps1

import telebot
import os

API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

id_list = ['Mechu', 'Carmen']


@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Hola, mis comandos son /start, /add, /delete \n/start comienza el chat \n/add te guardo en la lista de mensajes \n/delete te borro de la lista de mensajes')



@bot.message_handler(commands=['add'])
def start(message):
	id_nuevo = message.chat.id
	id_list.append(id_nuevo)

	bot.send_message(message.chat.id, f'la lista acuatilizada es {id_list}')



@bot.message_handler(commands=['delete'])
def start(message):
	id_delete = message.chat.id
	id_list.remove(id_delete)
	bot.send_message(message.chat.id, f'Fuiste removido de la lista de mensajes \nNueva lista {id_list}')

bot.polling()








# id_list = [1, 2, 3, 4, 5]
 
# def tele_bot(hour,i):
# 	hour = hour
# 	i = i
# 	msg = f'Hay Turno de consulado para Pasaporte Hora: {hour}'
	
# 	for i in range(len(id_list)):

# 		bot.send_message(id_list[i], f'{msg}')





# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
