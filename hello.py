import telebot

bot = telebot.TeleBot("1884845165:AAE51LVnKOW2_tmgXyCpsC1nu-a-JXIYBuc")

## Приветствие и получение номера жертвы#############################################

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Введите номер жертвы  вида - \"+7..........\"")

@bot.message_handler(content_types =['text'])	
def send_echo(message):
	parametr_number = message.text	
	bot.send_message(message.chat.id, "Номер жертвы - ", parametr_number, "\n", "Введите продолжительность атаки в секундах")
#####################################################################################

##Получение параметров атаки#########################################################




bot.polling( none_stop = True) 