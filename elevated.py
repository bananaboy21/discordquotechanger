import json
import os
from termcolor import colored
import colorama
import platform
import getpass

config = []

#L. 1-90 in main.py. This is L. 91+
print(colored("[ SUCCESS ] Elevated console permissions. Continuing execution...","green"))
print(colored("[ INIT ] Regrabbing config...","yellow"))

with open("temp.json") as i:
    config = json.load(i)

print(colored("[ SUCCESS ] Grabbed the config.","green"))
