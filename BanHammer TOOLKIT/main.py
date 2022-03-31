import colorama
import json
import ctypes
import os
import time


class ping:
    def main(self, IP):
        print(colorama.Fore.GREEN + "Pinging " + IP + "...")
        os.system("ping -c 1 " + IP)




class Menu:
    def __init__(self):
        self.fileName = "config.txt"
    ctypes.windll.kernel32.SetConsoleTitleW("BanHammer TOOLKIT v1.0") 
    def main(self):
        logo = """
        ███████████████████████████████████████████████████████████████████████████████████████████████████
        █▄─▄─▀██▀▄─██▄─▀█▄─▄█─█─██▀▄─██▄─▀█▀─▄█▄─▀█▀─▄█▄─▄▄─█▄─▄▄▀███─▄─▄─█─▄▄─█─▄▄─█▄─▄███▄─█─▄█▄─▄█─▄─▄─█
        ██─▄─▀██─▀─███─█▄▀─██─▄─██─▀─███─█▄█─███─█▄█─███─▄█▀██─▄─▄█████─███─██─█─██─██─██▀██─▄▀███─████─███
        ▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▄▀▀
        """

        main_menu = """
                                    +------------+---------+----------+
                                    |   Tools    | Version | Working? |
                                    +============+=========+==========+
                                    | Ping       |     1.0 | ✅       |
                                    | Portscan   |     1.0 | ✅       |
                                    | BTCStealer |     2.5 | ✅       |
                                    +------------+---------+----------+
        """
        
        self.slowType(logo, 0.001, False)
        self.slowType(main_menu, 0.002, False)
        input_command = input("\n> ")
        self.console(command = input_command)
    def reopen_console(self):
        command = input("\n> ")
        self.console(command=command)


    def slowType(self, text, speed, newLine = True):
            for i in text:
                print(i, end = "", flush = True)
                time.sleep(speed)
            if newLine:
                print()
                
    def console(self,command):
        if command == 'help':
            print("""
            Commands:
            ping - Ping a host
            portscan - Scan for ports
            BTCStealer - Steal BTC
            help - Show this help
            clear - Clear the console
            exit - Exit the console
            """)
            self.reopen_console()
        #check if a command has passed to the console
        if command == 'ping':
            print("""
            Usage:
            ping <host>
            """)
            self.reopen_console()
        if command == 'portscan':
            print("Portscan is currently not working")
            self.reopen_console()
        if command == 'BTCStealer':
            print("BTCStealer is currently not working")
            self.reopen_console()
        if command == 'clear':
            os.system('cls')
            self.main()
        if command == 'exit':
            exit()
        
if __name__ == '__main__':
    menu = Menu()
    menu.main()