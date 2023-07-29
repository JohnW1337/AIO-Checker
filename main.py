import requests
import os, requests
from time import strftime, gmtime,time
from tkinter import filedialog
from colorama import Fore

from os import system, name

os.system("title JohnW#1014 - v0.1")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():

    clear()
    print("                   -  AIO Team - ")
    print()
    print("")
    print(f""" 
    [{Fore.WHITE}1{Fore.WHITE}] Modules
    [{Fore.WHITE}2{Fore.WHITE}] Download Proxies
    [{Fore.WHITE}3{Fore.WHITE}] Mail (Checker)
    [{Fore.WHITE}4{Fore.WHITE}] Info

    [{Fore.WHITE}X{Fore.WHITE}] Exit""")
    try:
        questi = input(f"    [{Fore.WHITE}>{Fore.WHITE}] ").lower()
    except Exception:
        print("Invalid Input...")
        time.sleep(3)
        main()
    if questi == "1":
        import Modules
    elif questi == "2":
        import proxy
    elif questi == "3":
        import mail
    elif questi == "4":
        import mail
    elif questi == "x":
        os._exit(0)
main()
