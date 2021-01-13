import cryptocompare
from playsound import playsound
from colorama import init, AnsiToWin32, Fore, Back
import os
from time import sleep
import sys
#Made By Sahand Sabet (Sa-Sa.ir)

os.system('cls')
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
#Made By Sahand Sabet (Sa-Sa.ir)

def print_sasa():
    print(Fore.CYAN,"""
               ____                  ____        
              / ___|  __ _          / ___|  __ _ 
              \___ \ / _` |  _____  \___ \ / _` |
               ___) | (_| | |_____|  ___) | (_| |
              |____/ \__,_|         |____/ \__,_|
                                       
    """,file=stream)
#Made By Sahand Sabet (Sa-Sa.ir)
    
print_sasa();
BTC = cryptocompare.get_price('BTC',curr='USD')["BTC"]["USD"]
print(Fore.YELLOW," => BitCoin Price:",BTC,file=stream)
print(Fore.WHITE,file=stream)
#Made By Sahand Sabet (Sa-Sa.ir)
mini = int(input("  => Minimum price: "))
maxi = int(input("  => Maximum price: "))
os.system('cls')
print_sasa();
#Made By Sahand Sabet (Sa-Sa.ir)

while True:
    BTC = cryptocompare.get_price('BTC',curr='USD')["BTC"]["USD"]
    if BTC >= maxi:
        print(Fore.RED," => BitCoin Price:",BTC,file=stream)
        playsound('audio.mp3')
    elif BTC <= mini:
        print(Fore.RED," => BitCoin Price:",BTC,file=stream)
        playsound('audio.mp3')
    else :
        print(Fore.GREEN," => BitCoin Price:",BTC,file=stream)
    sleep(10)
    os.system('cls')
    print_sasa();
    #Made By Sahand Sabet (Sa-Sa.ir)
