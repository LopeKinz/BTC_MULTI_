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
        try:   
            r = requests.get(f"http://pinkyhaxssm.de/beta/check/{address}")
            try:
                if zero in r.text or l in r.text:
                    print("ok")
                    end = time.time()
                    print(f"{Fore.LIGHTYELLOW_EX} Thread %d = {Fore.YELLOW}PubKey: {address} |PrivKey : {privadress} | Balance : 0 |{Fore.MAGENTA} Processtime : {int(math.ceil(end - start))} sec" % i)

                if error1 in r.text or error2 in r.text:
                    print(f"{Fore.RED}Error #1 NO_API_CONNECTION or Error #2 API_UNDER_MAINTANCE")
                if hit in r.text:
                    print(f"{Fore.GREEN}HIT! PubKey: {address} |PrivKey : {privadress}| Results : {r.text}")
                    time.sleep(60)
                else:
                    print(r.text)
            except:
                print(r.text)
                break
        except:
            print(r.text)
            with open('logs.txt', 'w') as the_filed:
                the_filed.write(f'{r.text}\n')

main_menu = '''

    ____ ____________   _____ __             __         
   / __ )_  __/ ____/  / ___// /____  ____ _/ /__  _____
  / __  |/ / / /       \__ \/ __/ _ \/ __ `/ / _ \/ ___/
 / /_/ // / / /___    ___/ / /_/  __/ /_/ / /  __/ /    
/_____//_/  \____/   /____/\__/\___/\__,_/_/\___/_/     
            By Pinkyhax and BanHammer Team
                    BETA v3                     
'''

trues = "true"

print(main_menu)
token = input("Enter Token: ")
r = requests.get(f"http://pinkyhaxssm.de/auth/check/{token}")
print(r.text)
if r.text == trues:
    try:    
        online1 = requests.get("http://pinkyhaxssm.de/beta/status")
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
else:
    print("NO valid Premium key Found")
    time.sleep(10)
    sys.exit()