import os
import pyfiglet
import argparse
import subprocess

# ----
def grab_cc(path):
    print('[ CREDIT CARDS ]')
    with open('websites/CCards.txt', 'r') as f:
        words = f.readlines()
    for w in words:
        word = w.strip()
        print(f'[!] Word looking for: {word}')
        command = f"grep -rI '{word}' {path} | grep -n --color=auto 'Autofill.txt'"
        subprocess.run(command, shell=True)
# ----

# ---------
def main():
    ascii_banner = pyfiglet.figlet_format("4x0r-b17")
    print(ascii_banner)

    parser = argparse.ArgumentParser(description='[!] Search for a word in the folder provided')
    parser.add_argument('-p', '--path', type=str, required=True, help="Folder path to search in.")
    args = parser.parse_args()

    if os.path.isdir(args.path):
        grab_cc(args.path)

    else:
        print(f"[!] Error: {args.path} is not a valid directory.")
# ---------

if __name__ == "__main__":
    main()