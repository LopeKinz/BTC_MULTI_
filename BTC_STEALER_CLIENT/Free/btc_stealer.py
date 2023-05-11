from bitcoin import *
import requests
import time
import json
from colorama import Style , Fore , init
try:    # if is python3
    from urllib.request import urlopen
except: # if is python2
    from urllib2 import urlopen
import platform,socket,re,uuid,psutil,logging
from threading import Thread, Lock
import math
from pathlib import Path

path = str(Path.home() / "BTC")


zero = '[{}]'
l = "null"
error1 = "Internal"
error2 = "maintance"
hit = "balance"
version = 2



def server(i):
    while True:
        start = time.time()
        private_key = random_key()
        public_key = privtopub(private_key)
        address = pubtoaddr(public_key)
        privadress = privkey_to_address(private_key)
        time.sleep(0.5)
        r = requests.get(f"http://127.0.0.1:8000/beta/check/{address}")
        try:   
            if zero in r.text or l in r.text:
                    print("ok")
                    end = time.time()
                    print(f"{Fore.LIGHTYELLOW_EX} Thread %d = {Fore.YELLOW}PubKey: {address} |PrivKey : {privadress} | Balance : 0 |{Fore.MAGENTA} Processtime : {int(math.ceil(end - start))} sec" % i)

            if error1 in r.text or error2 in r.text:
                print(f"{Fore.RED}Error #1 NO_API_CONNECTION or Error #2 API_UNDER_MAINTANCE")
                with open('logs.txt', 'w') as the_filed:
                    the_filed.write(f'{r.text}\n')
            if hit in r.text:
                    print(f"{Fore.GREEN}HIT! PubKey: {address} |PrivKey : {privadress}| Results : {r.text}")
                    time.sleep(60)
            else:
                print(r.text)
        except:
            print(r.text)


main_menu = '''

    ____ ____________   _____ __             __         
   / __ )_  __/ ____/  / ___// /____  ____ _/ /__  _____
  / __  |/ / / /       \__ \/ __/ _ \/ __ `/ / _ \/ ___/
 / /_/ // / / /___    ___/ / /_/  __/ /_/ / /  __/ /    
/_____//_/  \____/   /____/\__/\___/\__,_/_/\___/_/     
            By Pinkyhax and BanHammer Team
                    BETA v3                     
'''


print(main_menu)
try:    
    online1 = requests.get("http://127.0.0.1:8000/beta/status")
    online = online1.text
    status1 = "Maintance"
    status2 = "Online"
    time.sleep(2)
    if status1 in online:
        print("Server is under Maintance")
        time.sleep(5)
        exit()
    if status2 in online:
        print("Server is Online")
        os.system("cls")
        threadss = input("Enter the number of threads!: ")
        for i in range(int(threadss)):
            t = Thread(target=server, args=(i,))
            t.start()
except requests.exceptions.ConnectionError:
    print("API Not Accessable!")
    time.sleep(10)
