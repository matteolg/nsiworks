import turtle
coté = int(input("Côté ? : "))
turtle.goto(0,0)
for i in range(4):
    turtle.forward(coté)
    turtle.left(90)
def fill():
    s = coté/5
    for i in range(5):
        turtle.forward(s)
        turtle.left(90)
s = coté/5        
turtle.begin_fill()      
fill()
turtle.end_fill()
turtle.forward(s)
fill()
turtle.right(90)
turtle.begin_fill()
fill()
turtle.end_fill
