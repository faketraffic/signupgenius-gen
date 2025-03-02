import requests
import random
import string
import json
import threading
from colorama import init, Fore

init(autoreset=True)

def info(msg):
    print(Fore.LIGHTBLACK_EX + '[*] ' + Fore.RESET + str(msg))

def error(msg):
    print(Fore.LIGHTRED_EX + '[-] ' + Fore.RESET + str(msg))

def okay(msg):
    print(Fore.LIGHTGREEN_EX + '[+] ' + Fore.RESET + str(msg))

def bombo():
    domains = ["lol.lol", "ok.ok", "china.best", "black.olo"]
    randomradom = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{randomradom}@{random.choice(domains)}"

def passsword():
    while True:
        password = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()", k=12))
        if any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in "!@#$%^&*()" for c in password) and all(password[i] != password[i+1] or password[i+1] != password[i+2] for i in range(len(password)-2)):
            return password

def gengen():
    while True:
        email = bombo()
        password = passsword()
        first_name = "Peter"
        last_name = "Rough"
        
        payload = {
            "email": email,
            "password": password,
            "firstname": first_name,
            "lastname": last_name,
            "loginuser": True,
            "companyname": ""
        }
        
        try:
            response = requests.post("https://www.signupgenius.com/SUGboxAPI.cfm?go=c.createMember", headers={
                "accept": "application/json, text/plain, */*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-GB,en;q=0.8",
                "cache-control": "no-cache",
                "content-type": "application/json, text/plain; charset=UTF-8",
                "origin": "https://www.signupgenius.com",
                "pragma": "no-cache",
                "referer": "https://www.signupgenius.com/",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Poop/133.0.0.0 Safari/537.36"
            }, json=payload)
            if response.status_code == 200:
                okay(f"{email}:{password}")
                with open("users.txt", "a") as file:
                    file.write(f"{email}:{password}\n")
            else:
                error(f"FAILED {response.status_code}")
        except Exception as e:
            error(f"Errored for some reason {str(e)}")

threads = []
for _ in range(10): #thread count btw
    thread = threading.Thread(target=gengen)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
