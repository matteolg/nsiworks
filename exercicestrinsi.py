from random import *
from time import *

def tri_insertion(t):
    for i in range(1,len(t)):
        x = t[i]
        j = i
    while j>0 and x<t[j-1]:
        t[j] = t[j-1]
        j = j-1
    t[j] = x
    return t

def tri_selection(t):
    for i in range(len(t)):
        vmin = t[i]
        imin = i
        for j in range(len(t)):
            if t[j]<vmin:
                vmin = t[j]
                imin = j
        temp = t[i]
        vmin = t[i]
        vmin = temp

def ttc(n, d):
    t = n*[0]
    for i in range(n):
        t[i] = randint(0, d)
    tri_insertion(t)
    return t

def test_tri_insertion():
    for i in range(0, 100):
        t1 = len[i]
        t2 = 2*i//5
        t3 = 2*i**2
        c1 = t1
        c2 = t2
        c3 = t3
        assert c1
        assert c2
        assert c3

def test_tri_selection():
    for i in range(0, 100):
        t1 = len[i]
        t2 = 2*i//5
        t3 = 2*i**2
        shuffle(t1)
        shuffle(t2)
        shuffle(t3)
        assert t1
        assert t2
        assert t3

def temps_tri_insertion():
    %temps = temps_tri_insertion

def temps_tri_selection():
    %temps = temps_tri_selection
