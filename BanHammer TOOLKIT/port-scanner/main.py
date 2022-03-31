#
# Made By diverse Lisenced To BanHammer
#

import os
import pyfiglet
import sys
import socket
from datetime import datetime

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

clear_console()
target = input('Please enter IPV4 adress: ')
clear_console()

print(f'Target: {target}\nPort Range: 1 - 65535')

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
         
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
        clear_console()
        print("Exiting...")
        sys.exit()

except socket.gaierror:
        clear_console()
        print("Hostname Could Not Be Resolved...")
        sys.exit()

except socket.error:
        clear_console()
        print("Server not responding...")
        sys.exit()