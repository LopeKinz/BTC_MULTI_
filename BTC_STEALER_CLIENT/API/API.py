import sys
import re
from time import sleep
from bitcoin import *
try:    # if is python3
    from urllib.request import urlopen
except: # if is python2
    from urllib2 import urlopen
from fastapi import FastAPI, Depends
import random
from datetime import datetime
import json
import requests


s = requests.Session()

app = FastAPI()


times = datetime.now()
dt_string = times.strftime("%d/%m/%Y %H:%M:%S")



zero = "[{}]"



class status():
    status: str

with open("status.json", "r") as f:
    current_status = json.load(f)['status']

@app.get('/beta/status')
def get_status():
    with open("status.json", "r") as f:
        current_status = json.load(f)['status']
    return current_status

@app.get("/version/{version}")
def version(version : int):
    return "Check for Updates!" if version < 2 else "Lastest Version Installed!"


@app.get('/beta/check/{address}')
def check_balance(address: str):
    try:
        wallet = s.get(f"https://api-r.bitcoinchain.com/v1/address/{address}", stream = True)
        response = wallet.json()
        return 0 if zero in response else response
    except:
        return("Could not Request Server!  API's ARE DOWN!")


    
@app.get('/auth/add/{token}')
def authadd(token: str):
    with open('tokens.json', 'r') as f:
        tokens = json.load(f)
        tokens[str(f"{token}")] = f"{token}"
    with open('tokens.json', 'w') as f:
        json.dump(tokens, f)
        return("Done!")
    
@app.get('/auth/remove/{token}')
def removeauth(token: str):
    with open('tokens.json', 'r') as f:
        tokens = json.load(f)
        tokens.pop(str(f"{token}"))
    with open('tokens.json', 'w') as f:
        json.dump(tokens, f)
        return("Done!")
    
@app.get('/auth/check/{token}')
def authcheck(token: str):
    with open('tokens.json', 'r') as f:
        tokens = json.load(f)
    return token in tokens