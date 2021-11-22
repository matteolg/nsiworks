from random import *
import sys
# 100

def pgpc(tab1, tab2):
    acc = 0
    pglen = 0
    if len(tab1)>len(tab2):
        pglen = len(tab2)
    else:
        pglen = len(tab1)
    for i in range(pglen):
        if tab1[i] != tab2[i]:
            acc = acc
        if tab1[i] == tab2[i]:
            acc+=1
        
    return "Le plus grand préfixe commun entre ces deux tableaux correspond à" + acc
pgpc([3, 4, 5, 6], [3, 4, 5, 9, 6])

# 101
def ordre(m1, m2):
    pg = 0
    result = None
    acc = 0
    change = 0
    if len(m1)>=len(m2):
        pg = len(m2)
    else:
        pg = len(m1)
    for i in range(pg):        
        while m1[i] != m2[i] and change == 0:
            acc+=1
            if acc ==1:
                if m2[i]>m1[i]:
                    result = True
                elif m1[i]>m2[i]:
                    result = False
                change = 1
                return result
ordre("abricot", "xilophone")
        
# 107

nb = randint(1, 50)
print("Devine le nombre !")
joueur = int(input(""))
if joueur == nb:
    print("Du premier coup, bravo !")
else:
    while joueur != nb:
        if joueur>= nb:
            print("Plus petit !")
        elif joueur<= nb:
            print("Plus grand !")
        joueur = int(input(""))
    print("Gagné !")

# 108

allumettes = 21
lastplayer = ""

while allumettes != 0:  
    joueur = int(input("Combien d'allumettes prenez-vous ? : "))
        
    while joueur != 1 and joueur !=2 and joueur !=3:
        print("Hé oh, il faut choisir entre 1 et 3 allumettes !")
        joueur = int(input("Combien d'allumettes prenez-vous ? : "))
               
    allumettes-= joueur
    
    lastplayer = joueur
    
    if allumettes <0 or allumettes == 0 and lastplayer == joueur:
        allumettes = 0
        print("Tu as perdu !")
        break
        
    ia = joueur+1
    
    if joueur == 3:
        ia = 3
    if allumettes == 2 or allumettes==1:
        ia = 1
    if allumettes == 3:
        ia = 2
    lastplayer = ia
        
    allumettes -= ia
    
    if allumettes <0 and lastplayer == ia:
        allumettes = 0
        print("Tu as gagné !")
    
    if allumettes > 0:
        print("L'IA a tiré", ia, "allumettes")
        print("Il reste", allumettes, "allumettes")
        
    
            