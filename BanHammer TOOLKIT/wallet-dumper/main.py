import os
import sys
import time
from bit import Key
from colorama import *

init()

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

royalty_address = ''
clear_console()
pwned_private_key = input(f'{Fore.GREEN}Input Private Key: ')
clear_console()
dump_to_address = input(f'{Fore.MAGENTA}Input Address To Dump To: ')
clear_console()

try:
    my_key = Key(pwned_private_key)
    totalbal = my_key.get_balance('usd')
    royalty_bal = int(totalbal) * 0.01

    dumped_bal = int(totalbal) - int(royalty_bal)

    print(f'{Fore.BLUE}Sending {Fore.YELLOW}{dumped_bal} USD{Fore.BLUE} to {dump_to_address}\nPaid {Fore.YELLOW}{royalty_bal} USD{Fore.BLUE} in fees!')

    outputs = [
        #royalty
        (royalty_address, royalty_bal, 'usd'),

        #dump address
        (dump_to_address, dumped_bal, 'usd')
    ]

    my_key.send(outputs)

except ValueError:
    clear_console()
    print(f'{Fore.RED}[ERROR] Invalid Private Key / Wallet is empty!')
    time.sleep(5)
    sys.exit()