import requests,time,re,os,sys
from colorama import Fore
from bs4 import BeautifulSoup
logo4 = """
\x1b[1;91m
\x1b[1;92m
\x1b[1;96m

█▀▀ █▀▀
█▄▄ █▄▄

█▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
█▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄
\x1b[1;93m
\x1b[1;92m         OWNER BY OKAMISPADE
\x1b[1;91m-----------------------------------------------
\x1b[1;97m> Author : Spade Dy(Original Coding)
\x1b[1;97m> Github : https://github.com/OkamiSpade
\x1b[1;97m> Facebok: Karque12
\x1b[1;97m> Version: CC GENERATOR
\x1b[0;97m-----------------------------------------------"""
print(logo4)

try:
	                mak = input("Limit number: ")
	                for i in range(int(mak)):
	                    print(Fore.YELLOW+'////////////////////////////////////////////')
	                    CC = requests.get('https://creditcardgenerator.money/', timeout=7).text
	                    gett = BeautifulSoup(CC, "html.parser")
	                    datax = gett.find('table', {'class':'cjo'})
	                    mal = re.findall('</label> </td><td><input type="text" value=(.*?) name=', CC)
	                    print(Fore.YELLOW+"Type: ",Fore.GREEN+mal[0])
	                    print(Fore.YELLOW+"CC Number:",Fore.GREEN+mal[1])
	                    print(Fore.YELLOW+"Validate:",Fore.GREEN+mal[2])
	                    print(Fore.YELLOW+"Name On:",Fore.GREEN+mal[3])
	                    print(Fore.YELLOW+"CCV Code:",Fore.GREEN+mal[4])
	                    print(Fore.YELLOW+"Balance ($):",Fore.GREEN+mal[5])
except: pass
	   
print(Fore.YELLOW+'////////////////////////////////////////////')
ulangin = input("Are you continue program? Y/N : ")
if ulangin=="y":
	os.system("python cc.py")
elif ulangin =="n":
	print(Fore.RED + "Stop This Run!!!" + Fore.WHITE)
	sys.exit()
