import string
import secrets
import os
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init

generated = 1
init(convert=True) # colorama init for windows

nitrogenAscii = """.__   __.  __  .___________..______        ______     _______  _______ .__   __. 
|  \ |  | |  | |           ||   _  \      /  __  \   /  _____||   ____||  \ |  | 
|   \|  | |  | `---|  |----`|  |_)  |    |  |  |  | |  |  __  |  |__   |   \|  | 
|  . `  | |  |     |  |     |      /     |  |  |  | |  | |_ | |   __|  |  . `  | 
|  |\   | |  |     |  |     |  |\  \----.|  `--'  | |  |__| | |  |____ |  |\   | 
|__| \__| |__|     |__|     | _| `._____| \______/   \______| |_______||__| \__|"""
vacWTF = "                           AS SEEN ON VACBAN.WTF\n                       https://github.com/luixiuno"

def nitrogen(letters_and_digits = string.ascii_letters + string.digits, N=16):
    while True:
        f = open("nitros.txt", "a")
        f.write("\nhttps://discord.gift/" + ''.join((secrets.choice(letters_and_digits) for _ in range(N))))
        f.close

def main():
    os.system("cls")
    print(Fore.GREEN + nitrogenAscii)
    print("\n")
    print(Fore.WHITE + vacWTF)
    with open("nitros.txt",'r+') as file:
      file.truncate(0)
    f = open("nitros.txt", "a")
    f.write(nitrogenAscii + "\n" + vacWTF)
    f.close()
    threads = input(Fore.WHITE + "\nThreads (Higher thread count = more cpu usage): ")
    executor = ThreadPoolExecutor(int(threads))
    future = executor.submit(nitrogen)
    future.result() # wait for the future to complete

# random string with characters picked from ascii_lowercase
if __name__ == "__main__":
    main()
else:
    raise Exception("Why are you importing this? Just run it. (main.py)")