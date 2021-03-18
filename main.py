#Open with double click on source or you CMD. Do NOT run with idle or ...

import cryptocompare
from playsound import playsound
from colorama import init, AnsiToWin32, Fore, Back
import os
from time import sleep
from tkinter import messagebox
import sys
#Made By Sahand Sabet (Sa-Sa.ir)

os.system('cls')
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
#Made By Sahand Sabet (Sa-Sa.ir)

def s_message(kind,title,msg):
    f = open("Source/Data/logs.txt", "a+")
    f.write(str(msg)+"\n")
    f.close()
    root = tk.Tk()
    root.withdraw()
    if kind == "Error":
        messagebox.showerror(str(title), str(msg))
    elif kind == "Info":
        messagebox.showinfo(str(title), str(msg))
    elif kind == "Warning":
        messagebox.showwarning(str(title), str(msg))
    root.destroy()

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
mini = int(input("  => Minimum price   : "))
maxi = int(input("  => Maximum price   : "))
time = int(input("  => Sleeping time(S): "))
os.system('cls')
print_sasa();
#Made By Sahand Sabet (Sa-Sa.ir)

while True:
    BTC = cryptocompare.get_price('BTC',curr='USD')["BTC"]["USD"]
    if BTC >= maxi or BTC <= mini:
        print(Fore.RED," => BitCoin Price:",BTC,file=stream)
        playsound('audio.mp3')
        s_message("Warning","Bitcoin Price","Bitcoin Price Got A Change .")
    else :
        print(Fore.GREEN," => BitCoin Price:",BTC,file=stream)
    sleep(time)
    os.system('cls')
    print_sasa();
    #Made By Sahand Sabet (Sa-Sa.ir)
