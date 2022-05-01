
from smtplib import OLDSTYLE_AUTH
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

canvas = Canvas(window, width = 70, height = 60, bg='white')
canvasmairie = Canvas(window, width=70, height=60, bg='white')
canvasmaison = Canvas(window, width=50, height=40, bg='white')

notenoughmoney = Label(window, text="monnaie insuffisante !", font= ("Arial", 20), bg='white', fg='red')
mairie = PhotoImage(file='Mairie.png').subsample(4)
bonhomme = PhotoImage(file='Stick.png').subsample(15)
housepicture = PhotoImage(file='House.png').subsample(15)
moneyvalue = 0
moneydisplay = Label(window, text=(moneyvalue, "$"), font= ("Arial", 40), bg='white', fg='black')
old_x, old_y = 0, 0


def clickerf():
    global moneyvalue
    moneyvalue += 50
    moneydisplay.configure(text=(moneyvalue, "$"), font= ("Arial", 40), bg='white', fg='black')
    moneydisplay.place(x=850, y=0)


def clic(event):
    global old_x, old_y
    old_x = event.x
    old_y = event.y
    canvasmaison.place(x=event.x, y=event.y)
    canvasmaison.create_image(25, 22, image=housepicture)
    window.unbind("<Button-1>")

def destroytext():
    notenoughmoney.place_forget()

def cooldown():
    global moneyvalue
    moneyvalue+=60
    moneydisplay.configure(text=(moneyvalue, "$"), font= ("Arial", 40), bg='white', fg='black')

def house():
    global moneyvalue
    if moneyvalue < 3000:    
        notenoughmoney.place(x=425, y=275)
        notenoughmoney.after(2000, destroytext)

    elif moneyvalue >= 3000: 
        window.bind("<Button-1>", clic)
        moneyvalue -= 3000
        moneydisplay.configure(text=(moneyvalue, "$"), font= ("Arial", 40), bg='white', fg='black')

        
        moneydisplay.after(3000, cooldown)
        
        

def game_start():
    global bonhomme
    # Après avoir cliqué sur "lancer la partie", l'interface se réinitialise
    frame.destroy()
    first_button.destroy()
    label_title.destroy()
    label_subtitle.destroy()
    window.config(background = '#FFFFFF')
    canvas.place(x=440, y=275)
    canvasmairie.place(x=500, y=275)
    canvasmairie.create_image(40, 30, image = mairie)
    canvas.create_image(37, 37, image=bonhomme)
    clicker = Button(window, text="Make money", command= clickerf)
    clicker.place(x=500, y=345)
    maison = Button(window, text="Placer une maison (3000$)", command=house)
    maison.place(x=920, y=690)
    



frame = Frame(window, bg='#2978E3', bd=10, relief=SUNKEN)

label_title = Label(frame, text = "City Mania", font= ("Arial", 40), bg='#2978E3', fg='white')
label_title.pack()

label_subtitle = Label(frame, text = "Bienvenue dans notre jeu en 2D", font= ("Arial", 25), bg='#2978E3', fg='white')
label_subtitle.pack()

first_button = Button(frame, text="Lancer la partie", font= ("Arial", 25), bg='white', fg='#2978E3', command=game_start)
first_button.pack(side=BOTTOM, pady=25)

frame.pack(expand=YES)

window.mainloop()