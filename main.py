import requests
import json
from random import choice
from colorama import Fore

uname = input("Author of the repo?\t")
reponame = input("Name of the repo?\t")

x = requests.get(f"https://api.github.com/repos/{uname}/{reponame}/stargazers") # to be continued :]
stargazer_names = []

for element in json.loads(x.content):
    stargazer_names.append(element["login"])

luckyone = choice(stargazer_names)

print("Luckiest person ever is:\t", Fore.GREEN, luckyone, Fore.RESET)
print("GitHub link of this lucky person:\t",Fore.BLUE, f"https://github.com/{luckyone}", Fore.RESET)
