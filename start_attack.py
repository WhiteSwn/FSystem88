import subprocess

def start_attack(parametr_time = 60, parametr_threads = 20, parametr_number):
""" Эта функция производит запуск файла Impusle.py с заданными параметрами  time, threads, number
	И возвращает сообщение об успешном запуске, либо о получении ошибки """

	command = "python impulse .py --method SMS --threads " + par_threads + " --time " + par_time + " --target " + par_number
	res = subprocess.call(command, shell = True)
	returned_output = subprocess.check_output(res) # returned_output содержит вывод в виде строки байтов
	print('Результат выполнения команды:', returned_output.decode("utf-8")) # Преобразуем байты в строку
	
	if """ Результат выпоолнеи якоманды положительный """ :
		return(True)
	else:
		return(False)	
