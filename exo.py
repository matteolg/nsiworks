from random import *

# Exercice 70
"""t = [5, 8, 10, 5, 10, 10]
def occurences(v, t):
    occ = 0
    for i in range(len(t)):
        if t[i] == v:
            occ+=1
    return occ
occurences(5, t)"""

# Exercice 71/72
"""t = [0]*100
vmax = t[0]
for i in range(len(t)):
    rand = randint(1, 1000)
    t[i] =rand 
    if t[i]>vmax:
        vmax = t[i]    
print(vmax)
print(t)"""

# Exercice 73
"""t = [0]*10
for i in range(len(t)):
    t[i]= randint(1, 10)
    
s = 0
for i in range(len(t)):   
    v = t[s]    
    s+=1

def occurences(v, t):
    occ = 0
    for i in range(len(t)):
        if t[i] == v:
            occ+=1
    print(t, occ)
occurences(7, t)"""

# Exercice 74
"""t = [1]*30
t[0] = 0
t[1] = 1
for i in range(2, len(t)):
    t[i] = t[i-1] + t[i-2]
    print(t[i])"""
    
#Exercice 75
"""t = [5]*20
def copie(t):
    v = [0]*len(t)
    for i in range(len(t)):
        v[i] = t[i]
    print(v)
copie(t)"""

#Exercice 76
"""v = [21, 65, 32]
t = [8, 14, 15]
def ajout(v, t):
    new = [0]*(len(t)+len(v))
    for i in range(len(t)):
        new[i] = t[i]
    for i in range(len(v)):
        new[i+len(t)] = v[i]
    print(new)
ajout(v, t)"""

# Exercice 77
"""t1 = [6, 3, 2, 1]
t2 = [89, 32, 3]
def concat(t1, t2):
    new = [0]*(len(t1)+len(t2))
    for i in range(len(t1)):
        new[i] = t1[i]
    for i in range(len(t2)):
        new[i+len(t1)] = t2[i]
    print(new)
concat(t1, t2)"""

# Exercice 78
"""def tableau_aleatoire(n, a, b):
    new = [0]*n
    for i in range(n):
        rand = randint(a,b)
        new[i] = rand
    print(new)
tableau_aleatoire(10, 15, 20)"""

# Exercice 79
def tableau_croissant(n):
    new = [0]*n
    for i in range(n):
        hasard = randint(80, 100)
        if hasard>new[i]:
            new[i] = hasard
        elif hasard <= new[i]:
            new[i] = new[i-1]
    print(new)
tableau_croissant(50) 
    
    
        
        


        
    

