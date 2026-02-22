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
    print(f"""{R}
  _____                ____                      
 |  __ \              |  _ \                     
 | |  | | ___ __  __  | |_) | ___  __ _ _ __  
 | |  | |/ _ \\ \/ /   |  _ < / _ \/ _` | '_ \ 
 | |__| | (_) >  <    | |_) |  __/ (_| | | | |
 |_____/ \___/_/\_\   |____/ \___|\__,_/_| |_|
    {W}Terminal OSINT Tool - {G}created by:Giorgi Tskrialashvili{W}
    {G}instagram: @only.giorgi404 
    {G}github: @onlygiorgi-20 
    """)
    print(f"{C}[1]{W} IP Geolocation")
    print(f"{C}[2]{W} Domain Resolver (DNS/IP)")
    print(f"{C}[3]{W} Social Media Hunter (Username)")
    print(f"{C}[4]{W} Port Scanner (Quick Scan)")
    print(f"{R}[0]{W} Exit Program\n")

def ip_geolocate():
    target = input(f"\n{Y}Enter IP Address: {W}")
    print(f"{C}Searching Database...{W}")
    try:
        data = requests.get(f"http://ip-api.com/json/{target}").json()
        if data['status'] == 'success':
            print(f"\n{G}[+] IP: {W}{data['query']}")
            print(f"{G}[+] Country: {W}{data['country']} ({data['countryCode']})")
            print(f"{G}[+] City: {W}{data['city']}")
            print(f"{G}[+] ISP: {W}{data['isp']}")
            print(f"{G}[+] Org: {W}{data['org']}")
        else:
            print(f"{R}[!] Error: Invalid IP address.{W}")
    except:
        print(f"{R}[!] Connection Error.{W}")
    input(f"\n{C}Press Enter to go back...{W}")

def domain_resolve():
    host = input(f"\n{Y}Enter Domain (e.g. site.com): {W}")
    try:
        ip_addr = socket.gethostbyname(host)
        print(f"\n{G}[+] Hostname: {W}{host}")
        print(f"{G}[+] Target IP: {W}{ip_addr}")
    except:
        print(f"{R}[!] Error: Could not resolve domain.{W}")
    input(f"\n{C}Press Enter to go back...{W}")

def social_hunter():
    user = input(f"\n{Y}Enter Target Username: {W}")
    links = [
        f"https://www.instagram.com/{user}",
        f"https://github.com/{user}",
        f"https://twitter.com/{user}",
        f"https://www.facebook.com/{user}"
    ]
    print(f"{C}Scanning Social Media profiles...{W}")
    for url in links:
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                print(f"{G}[FOUND] {W}{url}")
            else:
                print(f"{R}[NOT FOUND] {W}{url.split('/')[2]}")
        except:
            pass
    input(f"\n{C}Press Enter to go back...{W}")

def port_scanner():
    target = input(f"\n{Y}Enter IP or Domain: {W}")
    ports = [21, 22, 80, 443, 3306, 8080]
    print(f"{C}Scanning common ports...{W}")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{G}[+] Port {port}: OPEN{W}")
        s.close()
    input(f"\n{C}Press Enter to go back...{W}")

def main():
    while True:
        banner()
        choice = input(f"{R}DoxBean {C}> {W}")
        if choice == '1': ip_geolocate()
        elif choice == '2': domain_resolve()
        elif choice == '3': social_hunter()
        elif choice == '4': port_scanner()
        elif choice == '0': sys.exit()
        else: print(f"{R}Exiting... you for using DoxBean GOODBYE!{W}"); time.sleep(1)

if __name__ == "__main__":
    main()

