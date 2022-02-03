#ex 122
def ex122():
    t = [[(i*j) for j in range(11)] for i in range(11)]
    return t
#ex 123 
def ex123():
    t = [i for i in range(64)]
    m = [[(t[8*i+j]) for j in range(8)] for i in range(8)]
    return m
#ex 124
def ex124():
    m =[[(8*i+j) for j in range(8)] for i in range(8)]
    t = [0]*64
    for i in range(8):
        for j in range(8):
            t[8*i+j] = m[i][j]
    return t
#ex 125
from random import*   
def ex125():
    t = [[(randint(1,9999)) for j in range(30)] for i in range(30)]
    return t

#ex 126

def ex126():
    t = [[(randint(1,9999)) for j in range(30)] for i in range(30)]
    max = [0][0]
    for i in range(30):
        for j in range(30):
            if t[i][j] > max:
                max = t[i][j]
    return t, "/// Le maximum est", max


#ex 127

#creation d'une fonction minima qui trouve le minimum d'une ligne
def minima(t):
    v_min = t[0]
    for v in t:
            if v < v_min:
                v_min = v
    return v_min       

def ex127(n, m):
    v_max = 0
    g = [[(randint(1, 100)) for j in range(m)] for i in range(n)]
    print(g)
    for ligne in g:
        v_min = minima(ligne)
        if v_min > v_max:
            v_max = v_min
    return v_max

#ex 128
#1.

def grille_vide():
    g = [[(0) for c in range(7)] for l in range(6)]
    for ligne in g:
        for v in ligne:
            print(v, end = " ")
        print()    

#2.
        
def affiche(g):
    for l in range(6):
        for c in range(7):
            if g[-1-l][c] == 0:
                print(".", end = " ")
            elif g[l][c] == 1:
                print("X", end = " ")
            else:
                print("O", end = " ")
        print()
             
#3.

grille_test = [[(0) for c in range(7)] for l in range(6)]

def coup_possible(g, c):
    if g[5][c] != 0:
        return False
    else:
        return True
    
#4.
    
def jouer(g, j, c):
    i = 0
    while g[i][c] != 0:
        i += 1
    g[i][c] = j
    affiche(g)
    
#5.
    

    
    

    
        
        
    

    
    
    
    
    
    
    
    
    
    