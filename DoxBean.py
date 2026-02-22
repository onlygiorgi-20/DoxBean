import os
import sys
import socket
import requests
import time

# Colors
R = '\033[31m' # Red
G = '\033[32m' # Green
C = '\033[36m' # Cyan
W = '\033[0m'  # White
Y = '\033[33m' # Yellow

def banner():
    os.system('clear')
    print(r"""{0}
  _____                  ____                      
 |  __ \                |  _ \                     
 | |  | | ___  __  __   | |_) | ___  __ _ _ __  
 | |  | |/ _ \ \ \/ /   |  _ < / _ \/ _` | '_ \ 
 | |__| | (_) | >  <    | |_) |  __/ (_| | | | |
 |_____/ \___/ /_/\_\   |____/ \___|\__,_/_| |_|
    {1}Terminal OSINT Tool - {2}Created by: Giorgi Tskrialashvili{1}
     instagram:only.giorgi404
     github: onlygiorgi-20
     """.format(R, W, G))
    print(f"{C}[1]{W} IP location")
    print(f"{C}[2]{W} Domain Resolver")
    print(f"{C}[3]{W} Social Media Hunter")
    print(f"{C}[4]{W} Port Scanner")
    print(f"{R}[0]{W} Exit Program\n")

def ip_geolocate():
    target = input(f"\n{Y}Enter IP Address: {W}")
    try:
        data = requests.get(f"http://ip-api.com/json/{target}").json()
        if data['status'] == 'success':
            print(f"\n{G}[+] IP: {W}{data['query']}\n{G}[+] Country: {W}{data['country']}\n{G}[+] ISP: {W}{data['isp']}")
        else: print(f"{R}[!] Invalid IP.{W}")
    except: print(f"{R}[!] Connection Error.{W}")
    input(f"\n{C}Press Enter...{W}")

def domain_resolve():
    host = input(f"\n{Y}Enter Domain: {W}")
    try:
        print(f"\n{G}[+] IP: {W}{socket.gethostbyname(host)}")
    except: print(f"{R}[!] Error.{W}")
    input(f"\n{C}Press Enter...{W}")

def social_hunter():
    user = input(f"\n{Y}Enter Username: {W}")
    links = [f"https://www.instagram.com/{user}", f"https://github.com/{user}"]
    for url in links:
        try:
            if requests.get(url, timeout=5).status_code == 200: print(f"{G}[FOUND] {W}{url}")
            else: print(f"{R}[NOT] {W}{url.split('/')[2]}")
        except: pass
    input(f"\n{C}Press Enter...{W}")

def port_scanner():
    target = input(f"\n{Y}Enter IP: {W}")
    for port in [21, 22, 80, 443]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((target, port)) == 0: print(f"{G}[+] Port {port}: OPEN{W}")
        s.close()
    input(f"\n{C}Press Enter...{W}")

def main():
    while True:
        banner()
        choice = input(f"{R}DoxBean {C}> {W}")
        if choice == '1': ip_geolocate()
        elif choice == '2': domain_resolve()
        elif choice == '3': social_hunter()
        elif choice == '4': port_scanner()
        elif choice == '0':
            print(f"\n{G}Good Luck!{W}")
            break
        else:
            print(f"{R}EXITING... Thank you for using DoxBean GOODBYE!{W}")
            time.sleep(1)

if __name__ == "__main__":
    main()


