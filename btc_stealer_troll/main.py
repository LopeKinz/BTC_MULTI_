import webbrowser
from colorama import *
from bitcoin import *
url1 = 'https://www.youtube.com/watch?v=oiO29zJBkMo'

menu = """

██████╗ ████████╗ ██████╗    ███████╗████████╗███████╗ █████╗ ██╗     ███████╗██████╗ 
██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗
██████╔╝   ██║   ██║         ███████╗   ██║   █████╗  ███████║██║     █████╗  ██████╔╝
██╔══██╗   ██║   ██║         ╚════██║   ██║   ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗
██████╔╝   ██║   ╚██████╗    ███████║   ██║   ███████╗██║  ██║███████╗███████╗██║  ██║
╚═════╝    ╚═╝    ╚═════╝    ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                      
                                Early Accsess Version

"""

random_event = 0
print(menu)
while True:
    private_key = random_key()
    public_key = privtopub(private_key)
    address = pubtoaddr(public_key)
    privadress = privkey_to_address(private_key)
    print(f"{Fore.LIGHTYELLOW_EX} PubKey: {address} |PrivKey : {privadress} █████ {Fore.RED} Cracking {random.randint(0,999999999)}" )
    random_event = random.randint(0,999999)
    if random_event <= 1000:
        webbrowser.open(url1)