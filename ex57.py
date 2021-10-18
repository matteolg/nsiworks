from turtle import *

#EX 57
def test_Pythagore(a, b, c):
    if a**2+b**2 == c**2:
        return True
    else:
        return False
#EX 58
    
def valeur_absolue(a):
    if a>= 0:
        return a
    else:
        return -a
#EX 60 / 61
    
def max2(a, b):
    if a>b:
        result = a
    else:
        result = b
    return result

def max3(a, b, c):
    resultfinal = max2(max2(a, b), c)
    return resultfinal

#EX 62

def puissance(x, k):
    for i in range(k):
        acc = x*x
    if k==0:
        acc = 1
    return acc

#EX 63

def bissextile(a):
    if a%4 == 0 and a%100 != 0 or a%400 == 0:
        return True
    else:
        return False
#EX 64

def nbjoursannee(a):
    if bissextile(a) == True:
        return 366
    else:
        return 365
    
#EX 65
    
"""def nbjoursmois(a, m):"""
    
#EX 68
    
def triangle(n):
    begin_fill()
    for i in range(3):
        left(120)
        forward(n)
    left(120)
    end_fill()        
for i in range(3):
    triangle(100)
up()
goto(150, 0)
down()

    
        
    