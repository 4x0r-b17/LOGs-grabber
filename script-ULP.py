import os
import pyfiglet
import argparse
import subprocess

def grab_crypto(path):
    print('[ CRYPTO ]')
    with open('websites/crypto.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)


def grab_eCommerce(path):
    print('[ E-COMMERCE ]')
    with open('websites/eCommerces.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_emails(path):
    print('[ EMAILS ]')
    with open('websites/emails.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)
    
def grab_gaming(path):
    print('[ GAMING ]')
    with open('websites/gaming.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_giftcards(path):
    print('[ GIFT-CARDS ]')
    with open('websites/giftcards.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_learning(path):
    print('[ LEARNING ]')
    with open('websites/learning.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_payments(path):
    print('[ PAYMENTS ]')
    with open('websites/payments.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_rides(path):
    print('[ RIDES AND DELIVERY ]')
    with open('websites/rides.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_subscriptions(path):
    print('[ SUBSCRIPTIONS ]')
    with open('websites/subscriptions.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_travel(path):
    print('[ TRAVEL ]')
    with open('websites/travel.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_utility(path):
    print('[ UTILITY ]')
    with open('websites/utility.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_bett(path):
    print('[ BETTING ]')
    with open('websites/betting.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_passMan(path):
    print('[ PSWD MANAGER ]')
    with open('websites/passManager.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_porn(path):
    print('[ PORN ]')
    with open('websites/porn.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_tickets(path):
    print('[ TIKETS ]')
    with open('websites/tickets.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_cloud(path):
    print('[ CLOUD ]')
    with open('websites/cloud.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_wordlist(path):
    print('[ JUICY WORDLIST ]')
    with open('websites/wordlist.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        input(f'[!] Word looking for: {word}')
        command = f"grep '{word}' {path} -rnH --color=auto"
        subprocess.run(command, shell=True)

def grab_specific(path):
    print('[ SPECIFIC ]')
    word = input('[?] Insert the word to look for: ')
    command = f"grep '{word}' {path} -rnH --color=auto"
    subprocess.run(command, shell=True)

def grab_all(path):
    grab_crypto(path)
    grab_eCommerce(path)
    grab_emails(path)
    grab_gaming(path)
    grab_giftcards(path)
    grab_learning(path)
    grab_payments(path)
    grab_rides(path)
    grab_subscriptions(path)
    grab_travel(path)
    grab_utility(path)
    grab_bett(path)
    grab_passMan(path)
    grab_porn(path)
    grab_tickets(path)
    grab_cloud(path)
    grab_wordlist(path)
    grab_specific(path)
    
# ----

    

def create_output():
    pass

# ---------
def main():
    ascii_banner = pyfiglet.figlet_format("4x0r-b17")
    print(ascii_banner)

    parser = argparse.ArgumentParser(description='[!] Search for a word in the folder provided')
    parser.add_argument('-p', '--path', type=str, required=True, help="Folder path to search in.")
    args = parser.parse_args()

    if os.path.isdir(args.path):
        uSelection = input("""
    [?] Search for:
        
        [0]     crypto
        [1]     eCommerce
        [2]     email providers
        [3]     gaming wSites
        [4]     gift-cards wSites
        [5]     learning platforms
        [6]     payment wSites
        [7]     rides and delivery
        [8]     subscription based wSites
        [9]     travel wSites
        [10]    utlity wSites
        [11]    betting wSites
        [12]    password managers
        [13]    porn wSites
        [14]    tickets wSties
        [15]    juicy wordlist
        [16]    cloud sites
        [17]    specific word
        [333]   complete lookup
    
    [!] Select what to focus on: """)

        if int(uSelection) == 0:
            grab_crypto(args.path)
        elif int(uSelection) == 1:
            grab_eCommerce(args.path)
        elif int(uSelection) == 2:
            grab_emails(args.path)
        elif int(uSelection) == 3:
            grab_gaming(args.path)
        elif int(uSelection) == 4:
            grab_giftcards(args.path)
        elif int(uSelection) == 5:
            grab_learning(args.path)
        elif int(uSelection) == 6:
            grab_payments(args.path)
        elif int(uSelection) == 7:
            grab_rides(args.path)
        elif int(uSelection) == 8:
            grab_subscriptions(args.path)
        elif int(uSelection) == 9:
            grab_travel(args.path)
        elif int(uSelection) == 10:
            grab_utility(args.path)
        elif int(uSelection) == 11:
            grab_bett(args.path)
        elif int(uSelection) == 12:
            grab_passMan(args.path)
        elif int(uSelection) == 13:
            grab_porn(args.path)
        elif int(uSelection) == 14:
            grab_tickets(args.path)
        elif int(uSelection) == 15:
            grab_wordlist(args.path)
        elif int(uSelection) == 16:
            grab_cloud(args.path)
        elif int(uSelection) == 17:
            grab_specific(args.path)
        elif int(uSelection) == 333:
            grab_all(args.path)
        else:
            print('[!] Select an option')

    else:
        print(f"[!] Error: {args.path} is not a valid directory.")
# ---------

if __name__ == "__main__":
    main()