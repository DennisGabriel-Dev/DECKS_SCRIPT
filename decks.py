from fonte import *
import os, sys
os.system('clear')
print("----------------")
print("|DECKS's SCRIPT |")
print("|1 - Red Hawk   |")
print("|2 - SQLmap     |")
print("|3 - Nmap       |")
print("|4 - Xerxes     |")
print("|5 - Aircrack-ng|")
print("-----------------")
entrada = int(input(">"))
if entrada == 1:
  	redHawk()
if entrada == 2:
	sqlmap()
if entrada == 3:
	nmap()
if entrada == 4:
	xerxes()
if entrada == 5:
	aircrackng()
