import os
import time

print("Installing Requirements.....")
try:
    os.system("pip3 install bitcoin urllib3 datetime requests psutil colorama")
    time.sleep(2)

except:
    print("No Packages installed (Check your enviromental variables)")
