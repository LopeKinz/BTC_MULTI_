#
# Made By diverse Lisenced To BanHammer
#

import os
import string
import random
from requests import Session
from colorama import Fore, init

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

amount = int(input('How Many Codes To Generate: '))
clear_console()
print('Generating Codes Now!')

count=0
for _ in range(amount):
    count+=1
    code = "https://discordapp.com/gifts/%s" % (('').join(random.choices(string.ascii_letters + string.digits, k=16)))
    os.system(f'title Count: {count} Current: {code}')
    with open('codes.txt', 'a') as f:
        f.write('%s\n' % (code))

os.system(f'title Total Codes Created: {count}')
clear_console()
print('Output can be found in \'codes.txt\'')
input('\n\nPress Enter To Exit...')