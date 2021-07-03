import telebot

bot = telebot.TeleBot("1884845165:AAE51LVnKOW2_tmgXyCpsC1nu-a-JXIYBuc")

############################################################################################
## Приветствие и получение номера жертвы (number)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Введите номер жертвы  вида - \"+7..........\"")

@bot.message_handler(content_types =['text'])	
def send_number(message):
	parametr_number = message.text	
	bot.send_message(message.chat.id, "Номер жертвы - ", parametr_number, "\n", "Введите продолжительность атаки в секундах")
#####################################################################################

#############################################################################################
##Получение параметров атаки (time, threads)
@bot.message_handler(content_types =['text'])	
def send_time(message):
	parametr_time = message.text	
	bot.send_message(message.chat.id, "time - ", parametr_time, "\n", "Введите количество направлений атаки (threads)")

@bot.message_handler(content_types =['text'])	
def send_threads(message):
	parametr_time = message.text	
	bot.send_message(message.chat.id, "threads - ", parametr_time, "\n", "Чтобы начать атаку введите /attack")


##################################################################################################
## Начало атаки и запуск приложения Impulse
## Здесь необходимо вызвать функцию, которая запустит атаку

result_start_attack = start_attack(parametr_time, parametr_threads, parametr_number)

if result_start_attack == True:
	answer = "Атака началась, чтобы прервать отправьте \"стоп\""
else:
	answer = "Ошибка атаки, перезапустите бота"	

@bot.message_handler(content_types =['text'])	
def send_start_attack(message):
		bot.send_message(message.chat.id, answer)

#################################################################################################
## Вывод процесса атаки

#################################################################################################

## Прерывание атаки
@bot.message_handler(content_types =['text'])	
def send_stop_attack(message):
	if message.text == "Стоп":
		stop_attack()	
		bot.send_message(message.chat.id, "Атака остановлена")


################################################################################################

## сообщение о завершении атаки


################################################################################################


bot.polling( none_stop = True) 