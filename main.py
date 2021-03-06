from tkinter import *
from random import *
from sys import *
from time import *

# Lignes nécéssaires au lancement du programme :
window = Tk()
window.title("Jeu de plateau")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background = '#2978E3')

canvas = Canvas(window, width=1080, height=720, bg='white')
canvasmairie = Canvas(window, width=70, height=60, bg='white')
canvasmaison = Canvas(window, width=50, height=40, bg='white')
canvasusine = Canvas(window, width=50, height=50, bg='white')
notenoughmoney = Label(window, text="monnaie insuffisante !", font= ("Arial", 20), bg='white', fg='red')
mairie = PhotoImage(file='Mairie.png').subsample(4)
mairie_img = canvasmairie.create_image(40, 30, image = mairie)
bonhomme = PhotoImage(file='Stick.png').subsample(15)
bonhomme_img = canvas.create_image(37, 37, image=bonhomme)
house = PhotoImage(file='House.png').subsample(15)

usine = PhotoImage(file='Usine.png').subsample(15)
moneyvalue = 0
moneydisplay = Label(window, text=(moneyvalue, "$"), font= ("Arial", 40), bg='white', fg='black')
old_x, old_y = 0, 0
revenu = 500
price = 5000

def gauche(event):
    x = -10
    y = 0
    if (canvas.coords(bonhomme_img)[0]<27):
        canvas.move(bonhomme_img, 0, x)
    else:
        canvas.move(bonhomme_img, x, y)

    
def droite(event):
    x = 10
    y = 0
    if (canvas.coords(bonhomme_img)[0]>1057):
        canvas.move(bonhomme_img, 0, x)
    else:
        canvas.move(bonhomme_img, x, y)

def haut(event):
    x = 0
    y = -10
    if (canvas.coords(bonhomme_img)[1]<37):
        canvas.move(bonhomme_img, x, 0)
    else:
        canvas.move(bonhomme_img, x, y)

def bas(event):
    x = 0
    y = 10
    if (canvas.coords(bonhomme_img)[1]>687):
        canvas.move(bonhomme_img, x, 0)
    else:
        canvas.move(bonhomme_img, x, y)

def deplacement():
    window.bind("<Left>", gauche)
    window.bind("<Right>", droite)
    window.bind("<Up>", haut)
    window.bind("<Down>", bas)


def ameliorer(event):
    ky = canvasmaison.coords(house_img)
    print(ky)
    if (canvas.coords(bonhomme_img)[0]==canvasmaison.coords(house_img)[0]):
        print("hello")


def houseset():
    global moneyvalue
    if moneyvalue < 3000:    
        notenoughmoney.place(x=425, y=275)
        notenoughmoney.after(2000, destroytext)

    else: 
        window.bind("<Button-1>", clic_house)
        
        moneyvalue -= 3000
        moneydisplay.configure(text=(moneyvalue, "$"), font= ("Arial", 40), bg='white', fg='black')

        
        moneydisplay.after(3000, cooldown)

maisonbutton = Button(window, text="Placer une maison (3000$)", command=houseset)

def clickerf():
    global moneyvalue
    global revenu
    moneyvalue += revenu
    moneydisplay.configure(text=(moneyvalue, "$"), font= ("Arial", 40), bg='white', fg='black')
    moneydisplay.place(x=850, y=0)
    

def clic_house(event):
    global house_img
    global old_x, old_y
    old_x = event.x
    old_y = event.y
    canvasmaison.place(x=event.x, y=event.y)
    house_img = canvasmaison.create_image(25, 22, image = house)
    ameliorer(event)
    window.unbind("<Button-1>")
    maisonbutton.destroy()

    
def clic_factory(event):
    global old_x, old_y
    old_x = event.x
    old_y = event.y
    canvasusine.place(x=event.x, y=event.y)
    canvasusine.create_image(25, 22, image=usine)
    window.unbind("<Button-1>")
    usinebutton.destroy()
    

def destroytext():
    notenoughmoney.place_forget()

def cooldown():
    global moneyvalue
    moneyvalue+=150
    moneydisplay.configure(text=(moneyvalue, "$"), font= ("Arial", 40), bg='white', fg='black')
    moneydisplay.after(3000, cooldown)
    
def cooldownusine():
    global moneyvalue
    moneyvalue+=250
    moneydisplay.configure(text=(moneyvalue, "$"), font= ("Arial", 40), bg='white', fg='black')
    moneydisplay.after(5000, cooldownusine)


        
def factory():
    global moneyvalue
    if moneyvalue < 10000:    
        notenoughmoney.place(x=425, y=275)
        notenoughmoney.after(2000, destroytext)

    elif moneyvalue >= 10000:

        window.bind("<Button-1>", clic_factory)

        moneyvalue -= 10000
        moneydisplay.configure(text=(moneyvalue, "$"), font= ("Arial", 40), bg='white', fg='black')

        
        moneydisplay.after(3000, cooldownusine)

usinebutton = Button(window, text="Placer l'usine (10 000$)", command=factory)

def ameliorer_mairie():
    global price
    global moneyvalue
    global revenu
    if moneyvalue < price:    
        notenoughmoney.place(x=425, y=275)
        notenoughmoney.after(2000, destroytext)

    elif moneyvalue >= price:
        if price == 50*5000+35/100*5000:
            levelup.destroy()
        moneyvalue -= price
        revenu = revenu+20/100*revenu
        revenu = int(revenu)
        price = price+35/100*price
        price = int(price)
        moneydisplay.configure(text=(moneyvalue, "$"), font= ("Arial", 40), bg='white', fg='black')
        levelup['text'] = "Améliorer ("+str(price)+"$)"      

def game_start():
    global bonhomme
    # Après avoir cliqué sur "lancer la partie", l'interface se réinitialise
    frame.destroy()
    first_button.destroy()
    label_title.destroy()
    label_subtitle.destroy()
    
    window.config(background = '#FFFFFF')
    canvas.place(x=0, y=0)
    canvasmairie.place(x=500, y=275)
    
    
    deplacement()
    clicker = Button(window, text="Make money", command= clickerf)
    clicker.place(x=500, y=345)
    levelup.place(x=500, y=375)
    maisonbutton.place(x=920, y=690)
    usinebutton.place(x=700, y=690)
    

levelup = Button(window, text="Améliorer ("+str(price)+"$)", command=ameliorer_mairie)


frame = Frame(window, bg='#2978E3', bd=10, relief=SUNKEN)

label_title = Label(frame, text = "City Mania", font= ("Arial", 40), bg='#2978E3', fg='white')
label_title.pack()

label_subtitle = Label(frame, text = "Bienvenue dans notre jeu en 2D", font= ("Arial", 25), bg='#2978E3', fg='white')
label_subtitle.pack()

first_button = Button(frame, text="Lancer la partie", font= ("Arial", 25), bg='white', fg='#2978E3', command=game_start)
first_button.pack(side=BOTTOM, pady=25)
frame.pack(expand=YES)

window.mainloop()
