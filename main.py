import random
import string
import os
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore
generated = 1
def nitrogen(letters_and_digits = string.ascii_letters + string.digits, N=16):
    while True:
        letters_and_digits = string.ascii_letters + string.digits
        f = open("nitros.txt", "a")
        f.write("\nhttps://discord.gift/" + ''.join((random.choice(letters_and_digits) for i in range(N))))
        f.close
def main():
    os.system("cls")
    print(Fore.GREEN + """.__   __.  __  .___________..______        ______     _______  _______ .__   __. 
|  \ |  | |  | |           ||   _  \      /  __  \   /  _____||   ____||  \ |  | 
|   \|  | |  | `---|  |----`|  |_)  |    |  |  |  | |  |  __  |  |__   |   \|  | 
|  . `  | |  |     |  |     |      /     |  |  |  | |  | |_ | |   __|  |  . `  | 
|  |\   | |  |     |  |     |  |\  \----.|  `--'  | |  |__| | |  |____ |  |\   | 
|__| \__| |__|     |__|     | _| `._____| \______/   \______| |_______||__| \__|""")
    print("\n")
    print("                           AS SEEN ON VACBAN.WTF\n                       https://github.com/luixiuno")
    with open("nitros.txt",'r+') as file:
      file.truncate(0)
    f = open("nitros.txt", "a")
    f.write(""".__   __.  __  .___________..______        ______     _______  _______ .__   __. 
|  \ |  | |  | |           ||   _  \      /  __  \   /  _____||   ____||  \ |  | 
|   \|  | |  | `---|  |----`|  |_)  |    |  |  |  | |  |  __  |  |__   |   \|  | 
|  . `  | |  |     |  |     |      /     |  |  |  | |  | |_ | |   __|  |  . `  | 
|  |\   | |  |     |  |     |  |\  \----.|  `--'  | |  |__| | |  |____ |  |\   | 
|__| \__| |__|     |__|     | _| `._____| \______/   \______| |_______||__| \__|\n\n                           AS SEEN ON VACBAN.WTF\n                       https://github.com/luixiuno""")
    f.close()
    threads = input(Fore.WHITE + "\nThreads (FREE YOUR CPU SO THE THREADS CAN RUN SMOOOOOOTHLY): ")
    executor = ThreadPoolExecutor(int(threads))
    future = executor.submit(nitrogen)

# random string with characters picked from ascii_lowercase
if __name__ == "__main__":
    main()
    
else:
    raise Exception("WE DO NOT ALLOW SKIDDIES 💀💀💀 | WE DO NOT ALLOW SKIDDIES 💀💀💀 | WE DO NOT ALLOW SKIDDIES 💀💀💀 | WE DO NOT ALLOW SKIDDIES 💀💀💀")