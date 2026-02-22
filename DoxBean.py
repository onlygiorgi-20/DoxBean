import os
import sys
import socket
import requests
import time
import hashlib

# Standard Colors
R = '\033[31m' # Red
G = '\033[32m' # Green
C = '\033[36m' # Cyan
W = '\033[0m'  # White
Y = '\033[33m' # Yellow

def banner():
    os.system('clear')
    print(r"""{0}
  _____                ____                      
 |  __ \              |  _ \                     
 | |  | | ___ __  __  | |_) | ___  __ _ _ __  
 | |  | |/ _ \\ \/ /  |  _ < / _ \/ _` | '_ \ 
 | |__| | (_) >  <    | |_) |  __/ (_| | | | |
 |_____/ \___/_/\_\   |____/ \___|\__,_/_| |_|
 {1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {2}  Author:    Giorgi Tskrialashvili
 {2}  Instagram: only.giorgi404
 {2}  GitHub:    onlygiorgi-20
 {1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """.format(R, W, G))
    print(f"{C}[1]{W} IP Lookup         {C}[5]{W} HTTP Headers")
    print(f"{C}[2]{W} DNS Resolver      {C}[6]{W} MD5 Generator")
    print(f"{C}[3]{W} Social Finder     {C}[7]{W} User-Agent Info")
    print(f"{C}[4]{W} Port Scanner      {C}[8]{W} Network Info")
    print(f"{R}[0]{W} Exit\n")

def ip_lookup():
    ip = input(f"\n{Y}Enter IP: {W}")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        print(f"\n{G}[+] Country: {W}{r.get('country')}\n{G}[+] ISP: {W}{r.get('isp')}")
    except: print(f"{R}[!] Error{W}")
    input(f"\n{C}Press Enter...{W}")

def dns_resolve():
    domain = input(f"\n{Y}Enter Domain: {W}")
    try:
        print(f"{G}[+] IP: {W}{socket.gethostbyname(domain)}")
    except: print(f"{R}[!] Failed{W}")
    input(f"\n{C}Press Enter...{W}")

def social_find():
    u = input(f"\n{Y}Enter Username: {W}")
    sites = ["instagram.com", "github.com", "twitter.com"]
    for s in sites:
        try:
            if requests.get(f"https://{s}/{u}", timeout=3).status_code == 200:
                print(f"{G}[FOUND] {W}{s}")
            else: print(f"{R}[NOT FOUND] {W}{s}")
        except: pass
    input(f"\n{C}Press Enter...{W}")

def port_scan():
    host = input(f"\n{Y}Enter Host: {W}")
    for p in [80, 443, 22]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((host, p)) == 0: print(f"{G}[+] Port {p}: OPEN{W}")
        s.close()
    input(f"\n{C}Press Enter...{W}")

def http_headers():
    url = input(f"\n{Y}Enter URL: {W}")
    try:
        h = requests.get(url).headers
        for k, v in h.items(): print(f"{G}{k}: {W}{v}")
    except: print(f"{R}[!] Error{W}")
    input(f"\n{C}Press Enter...{W}")

def hash_gen():
    txt = input(f"\n{Y}Text: {W}")
    print(f"{G}MD5: {W}{hashlib.md5(txt.encode()).hexdigest()}")
    input(f"\n{C}Press Enter...{W}")

def user_agent():
    ua = requests.get("https://httpbin.org/user-agent").json()
    print(f"\n{G}Your Agent: {W}{ua['user-agent']}")
    input(f"\n{C}Press Enter...{W}")

def network_info():
    name = socket.gethostname()
    print(f"\n{G}[+] Host: {W}{name}\n{G}[+] Local: {W}{socket.gethostbyname(name)}")
    input(f"\n{C}Press Enter...{W}")

def main():
    while True:
        banner()
        choice = input(f"{R}DoxBean {C}> {W}")
        if choice == '1': ip_lookup()
        elif choice == '2': dns_resolve()
        elif choice == '3': social_find()
        elif choice == '4': port_scan()
        elif choice == '5': http_headers()
        elif choice == '6': hash_gen()
        elif choice == '7': user_agent()
        elif choice == '8': network_info()
        elif choice == '0': break
        else: time.sleep(1)

if __name__ == "__main__":
    main()

