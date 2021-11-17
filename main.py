import requests
import json
from random import choice
from colorama import Fore
from sys import argv

uname = ""
reponame = ""

if len(argv) == 1:
    print("tip:\tyou can always use arguments like \"--uname --reponame --u --r -u -r\"")
    uname = input("Author of the repo?\t")
    reponame = input("Name of the repo?\t")

else:
    c = 0
    for arg in argv:
        
        if (arg == "--uname" or arg == "--u" or arg == "-u"):
            uname = argv[c + 1]
        
        if (arg == "--reponame" or arg == "--r" or arg == "-r"):
            reponame = argv[c + 1]

        c+=1

# If uname and reponame are still not changed.

if(uname == ""):
    print("You should pass an username.")
    exit(1)

if(reponame == ""):
    print("You should pass a reponame.")
    exit(1)

if(uname == "" and reponame == ""):
    print("You should pass an username and a reponame.")
    exit(1)

x = requests.get(f"https://api.github.com/repos/{uname}/{reponame}/stargazers") # to be continued :]
if x.status_code != 404:
    stargazer_names = []

    for element in json.loads(x.content):
        stargazer_names.append(element["login"])

    luckyone = choice(stargazer_names)

    print("Luckiest person ever is:\t", Fore.GREEN, luckyone, Fore.RESET)
    print("GitHub link of this lucky person:\t",Fore.BLUE, f"https://github.com/{luckyone}", Fore.RESET)

else:
    print("This user / repo doesn't exist.")
    exit(1)
