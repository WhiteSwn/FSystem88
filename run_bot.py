import subprocess
def start():
    res = subprocess.run(["python3 /home/kali/SpamTeleBot/bot.py"], shell=True)
    return(res)

