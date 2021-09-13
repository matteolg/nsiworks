import random

salaires = 12
year = 0
listesalaires = []
shuffle = 0

for i in range(salaires):
    wallet = random.randint(0, 10000)
    print(wallet)
    if wallet < 5000:
        print("Vous avez moins de 5000 euros ce mois-ci")
    elif wallet >= 5000:
        print("Vous avez 5000 euros ou plus!")
    year += wallet
    listesalaires.append(year)

print("Cette année, vous avez eu ", year, " euros !")
binary = bin(year)
print("En binaire", year," s'écrit ", binary, " !")

def rappel() :
    shuffle = random.randint(1, 2)
    if shuffle ==1:
        print("Voici la liste des salaires de cette année : ", listesalaires)
    elif shuffle ==2:
        random.shuffle(listesalaires)
        print("Voici la liste des salaires de cette année dans le désordre : ", listesalaires)

def longueur (a):
    print("Le mot contient", len(a), " caractères")

longueur("Informatique")
rappel()
