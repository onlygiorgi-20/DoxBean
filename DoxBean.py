import os
import sys
import socket
import requests

# Colors for professional look
R = '\033[31m' # Red
G = '\033[32m' # Green
C = '\033[36m' # Cyan
W = '\033[0m'  # White

def banner():
    os.system('clear')
    print(f"""
  {C}
  ____                ____                      
 |  _ \  _____  __   | __ )  ___  __ _ _ __  
 | | | |/ _ \ \/ /   |  _ \ / _ \/ _` | '_ \ 
 | |_| | (_) >  <    | |_) |  __/ (_| | | | |
 |____/ \___/_/\_\   |____/ \___|\__,_|_| |_| v0.1{W}

 {G}Created by: Giorgi Tskrialashvili{W}
 {G}GitHub: @onlygiorgi-20  [+] {W}
 Discord: @only.giorgi      [+] {W} 
 instagram: @only.giorgi404 [+] {W}
 --------------------------------------------------
 {R}[1]{W} Information Gathering   {R}[2]{W} Password Attacks
 {R}[3]{W} Wireless Testing        {R}[4]{W} Exploitation Tools
 {R}[5]{W} Sniffing & Spoofing     {R}[6]{W} Web Hacking
 {R}[7]{W} Private Web Hacking     {R}[8]{W} Post Exploitation
 {R}[9]{W} My IP                   {R}[10]{W} IP Tracker
 {R}[11]{W} Phone Number Tracker   {R}[0]{W} INSTALL & UPDATE
 {R}[12]{W} CONTRIBUTORS           {R}[99]{W} EXIT
 --------------------------------------------------
    """)

def get_my_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
        print(f"\n{G}[+]{W} Your Public IP: {C}{ip}{W}")
    except:
        print(f"\n{R}[!]{W} Connection Error!")
    input("\nPress Enter to go back...")

def ip_tracker():
    target = input(f"\n{G}[?]{W} Enter Target IP: ")
    try:
        response = requests.get(f"http://ip-api.com/json/{target}").json()
        print(f"\n{C}--- Results ---{W}")
        print(f"Status: {response['status']}")
        print(f"Country: {response['country']}")
        print(f"City: {response['city']}")
        print(f"ISP: {response['isp']}")
    except:
        print(f"\n{R}[!]{W} Invalid IP or Connection Issue!")
    input("\nPress Enter to go back...")

def main():
    while True:
        banner()
        choice = input(f"{G}DoxBean > {W}")

        if choice == '1':
            print(f"\n{C}[*]{W} Loading Info Gathering Modules...")
            # Here you can call: os.system('nmap -v')
        elif choice == '9':
            get_my_ip()
        elif choice == '10':
            ip_tracker()
        elif choice == '0':
            print(f"\n{G}[*]{W} Updating DoxBean...")
            os.system('git pull')
        elif choice == '99':
            print(f"\n{R}Exiting DoxBean... thank you for using DoxBean Goodbye!{W}")
            sys.exit()
        else:
            print(f"\n{R}[!] Invalid Option!{W}")
            os.system('sleep 1')

if __name__ == "__main__":
    main()
