import json
import os
from termcolor import colored
import colorama
import platform
import getpass
from elevate import elevate



config = []
syst = None
quotesdir = ""
success = None
colorama.init()

print(colored("[ START ] Detecting if console is elevated..","yellow"))

if os.getuid() == 0:
    import elevated
    elevated


print(colored("[ INIT ] Trying to detect config...","yellow"))


with open("config.json") as i:
    config = json.load(i)


print(colored("[ INIT ] Successfully loaded config. Detecting operating system...","yellow"))

if platform.system() == "Linux":
    syst = "L"
elif platform.system() == "Windows":
    syst = "W"
elif platform.system() == "Java":
    syst = "M"
else:
    print(colored("[ FATAL ] Failed to detect operating system. Please make sure Python can access the system's information","red"))
    exit()



print(colored(f"[ INIT ] Operating system detected ({platform.system()}).","green"))
dt = input("Canary or Stable? (c/s) ")
if not dt.lower() == "c" and not dt.lower() == "s":
    print(colored("[ ERR ] Invalid input. Aborting..","red"))
    exit()

print(colored("[ INIT ] Detecting quotes.json","green"))
if dt.lower() == "c":
    if syst == "L":
        dirposs = (config['DirLinCan']).split("USER")
        dirposs = f"{getpass.getuser()}".join(dirposs)
        if os.path.isfile(f"{dirposs}quotes.json"):
            quotesdir = f"{config['DirLinCan']}quotes.json"
            success = True
        else:
            success = False
    #TODO: Add Windows and Mac OS X crap.
else:
    if syst == "L":
        dirposs = (config['DirLinCan']).split("USER")
        dirposs = f"{getpass.getuser()}".join(dirposs)
        if os.path.exists(f"{dirposs}quotes.json"):
            quotesdir = f"{dirposs}quotes.json"
            success = True
        else:
            success = False
    #TODO: Add Windows and Mac OS X crap. Fun!

if success == False:
    print(colored("[ ERR ] Could not find the quotes.json file. Make sure that Discord is installed in the default directory, and that Python has access to read the files.","red"))
    exit()

print(colored("[ WARN ] Attempting to save information for elevating console. Please do not stop the script..","yellow"))


config.update({"dirposs": dirposs})
with open("temp.json","w+") as fp:
    dumped = json.dumps(config)
    fp.write(dumped)

print(colored("[ INIT ] Attemping to elevate console permissions. On prompted, please press Yes. If needed, enter the admin password. If failed, the program will restart.","green"))

if syst == "W":
    elevate(show_console=False)
else:
    elevate(graphical=False)
