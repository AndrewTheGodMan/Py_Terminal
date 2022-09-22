from tqdm import tqdm
import time
import getpass
from settings import *
buildnum = "1.0.2"

def NLS(numto,wait):
    for i in tqdm(range(numto)):
        time.sleep(wait)

def load():
    for i in tqdm(range(100)):
        time.sleep(0.1)

def load2():
    for i in tqdm(range(10)):
        time.sleep(0.2)

def terminal():
    load2()
    print("PREPING TERMINAL MAIN.PY")
    load2()
    print("")
    print("")
    print("WELCOME TO CODE RED - V:"+ buildnum)
    print("SIGNED IN AS - "+ userid.upper())
    def oof():
        code123 = input("CODE RED "+ buildnum +" ~ ")
        def code():
            if code123 == "close":
                print("CLOSING")
            elif code123 == "hack":
                hack2 = input("WHO DO YOU WANT TO HACK : ")
                hack = hack2.upper()
                time.sleep(0.2)
                IP2 = input("WHAT IS THE IP OF THE DATABASE YOU WANT TO HACK "+hack+" ON : ")
                IP = IP2.upper()
                time.sleep(0.1)
                load2()
                print("HACKING " + hack + " ON THE IP : "+ IP)
                time.sleep(0.5)
                load()
                time.sleep(0.3)
                print("HACKED " + hack + " ON THE IP : "+ IP)
                print("")
                oof()
            
            elif code123 == "clear":
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                oof()

            elif code123 == "cmds":
                print("COMMANDS : cmds, close, hack")
                print("")
                oof()

            elif code123 ==  "":
                oof()
            
            else: 
                print("COMMAND NOT ON SERVER")
                oof()
        code()
    oof()



def login():
    password_input = getpass.getpass('PASSWORD:')
    time.sleep(0.3)
    load2()
    time.sleep(0.1)
    if password_input == password:
        print("CORRECT PASSWORD ")
        terminal()
    else:
        print("INCORRECT PASSWORD ")
        time.sleep(0.1)
        def login2():
            password_input = getpass.getpass('PASSWORD:')
            time.sleep(0.3)
            load2()
            time.sleep(0.1)
            def oooof():
                if password_input == password:
                    print("CORRECT PASSWORD ")
                    terminal()
                else:
                    print("INCORRECT PASSWORD ")
                    time.sleep(0.1)
                    login2()
            oooof()
        login2()

load()
print("SETTING UP")
time.sleep(1)
load()
print("LOGIN READY")
login()






