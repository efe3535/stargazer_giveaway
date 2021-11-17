import requests
import json
from random import choice
from colorama import Fore
from sys import argv

uname = ""
reponame = ""
stargazers_count = int()

if len(argv) == 1:
    print("tip:\tyou can always use arguments like \"--uname --reponame --u --r -u -r\"")
    uname = input("Author of the repo?\t")
    reponame = input("Name of the repo?\t")

if("--help" in argv):
    print("usage:\n--help:\tshows help\n--uname:\tusername for repo\n--reponame:\trepo name for repo")
    exit(0)

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
y = requests.get(f"https://api.github.com/repos/{uname}/{reponame}"); 

if(y.status_code != 404):
    stargazers_count = json.loads(y.content)["stargazers_count"]

if x.status_code != 404 and stargazers_count > 1: 
    stargazer_names = []

    for element in json.loads(x.content):
        stargazer_names.append(element["login"])
     
    luckyone = choice(stargazer_names)

    print("Luckiest person ever is:\t", Fore.GREEN, luckyone, Fore.RESET)
    print("GitHub link of this lucky person:\t",Fore.BLUE, f"https://github.com/{luckyone}", Fore.RESET)

else:
    if(stargazers_count == 0 and x.status_code != 404):
        print(f"This repo doesn't have enough stars for a giveaway... {Fore.BLUE}:({Fore.RESET}") 

    elif(x.status_code == 404):
        print(f"{Fore.RED}This user / repo doesn't exist.{Fore.RESET}")
        exit(1)

