import json
import requests
import time

choice = input("[1]Add User\n[2]Remove User\n[3]Check User\n[4]Exit\n")

if choice == "1":
    token = input("Enter Token: ")
    r = requests.get(f"http://127.0.0.1:8000/auth/add/{token}")
    print(r.text)
    time.sleep(10)
elif choice == "2":
    token = input("Enter Token: ")
    r = requests.get(f"http://127.0.0.1:8000/auth/remove/{token}")
    print(r.text)
    time.sleep(10)
elif choice == "3":
    token = input("Enter Token: ")
    r = requests.get(f"http://127.0.0.1:8000/auth/check/{token}")
    print(r.text)
    time.sleep(10)
elif choice == "4":
    exit()

r = requests.get(f"http://127.0.0.1:8000/auth/check/{token}/")