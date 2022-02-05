#!usr/bin/env python
import os
def redHawk():
	print("INSTALANDO REDHAWK \n")
	os.system('apt install git')
	os.system('apt install php -y')
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
def sqlmap():
	print("INSTALANDO SQLMAP \n")
	os.system('apt install git')
	os.system('apt install python -y')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
def nmap():
	print("INSTALANDO NMAP \n")
	os.system('apt install git')
	os.system('apt install nmap')
	print('OBS: Para acessar ao Nmap digite no terminal : nmap')
def xerxes():
	print("INSTALANDO XERXES \n")
	os.system('apt install clang')
	os.system('apt install git -y')
	os.system('git clone https://github.com/sepehrdaddev/Xerxes')

def aircrackng():
	print("INSTALANDO AIRCRACK-NG")
	os.system('apt install git -y')
	os.system('git clone https://github.com/aircrack-ng/aircrack-ng')
