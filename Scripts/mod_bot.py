# ./venv/Scripts/Activate.ps1

import telebot
from var_sv import wrt_nuevo, rde_list, api, wrt_list

API_KEY = api()
bot = telebot.TeleBot(API_KEY)


ids = open('D:\Documentos\Bot ciudadania\Textos\id_lista.txt', 'r')
reader = ids.readlines()
idl = []
for line in reader:
    idl.append(line.rstrip('\n'))

def tele(i, hour):
	for id in idl:
		bot .send_message(id,f'Hay turnos de consulado hora: {hour}')
		photo = open(f"D://Documentos//Bot ciudadania//screenshots//screen_{i}.png", 'rb')
		bot.send_photo(id, photo)


@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Hola, mis comandos son /start, /add, /delete \n/start comienza el chat \n/add te guardo en la lista de mensajes \n/delete te borro de la lista de mensajes')



@bot.message_handler(commands=['add'])
def start(message):
	id_nuevo = message.chat.id
	wrt_nuevo(id_nuevo)

	id_list = rde_list()
	bot.send_message(message.chat.id, f'la lista actualizada es {id_list}')



@bot.message_handler(commands=['delete'])
def start(message):

	id_list = rde_list()
	id_delete = str(message.chat.id)
	id_list.remove(id_delete)
	# tengo que reescribir la nueva lista con el id borrado
	wrt_list(id_list)
	bot.send_message(message.chat.id, f'Fuiste removido de la lista de mensajes \nNueva lista {id_list}')


#bot.polling()


