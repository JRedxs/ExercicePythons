#############################################################
#                                                           #
#                   VANDEVELDE ENZO                         #
#                      12-11-2022                           #
#                                                           #
#                                                           #
#                                                           #
#############################################################


from tkinter import *
import tkinter as tk
import datetime
import locale
import tkinter.font as font
import pytz
locale.setlocale(locale.LC_TIME, '')

date_actuelle = datetime.datetime.now()  # Récupération de l'heure actuelle

Fenetre = tk.Tk()  # Création de la fenêtre
Fenetre.geometry("300x500")  # Dimensions de la fenêtre
Fenetre.title("Horaire des pays")  # Titre de la fenêtre
Fenetre.configure(bg="black")  # Background de la fenêtre
Fenetre.resizable(width=False, height=False)  # On empeche l'agrandissement

StyleEcriture = font.Font(family='Arial', size=15, weight="bold")
Taille = font.Font(size=25)
TailleHeure = font.Font(size=18)
date = datetime.date.today()  # Récupération de la date du jour
day = datetime.date.today()
day1 = day.strftime('%A')

labelday = Label(Fenetre, text=day1.upper(),
                 background="Black", fg='White', font=Taille)
labelday.place(relx=0.3, rely=0.02)


# Fonction pour l'heure de Paris
def HeureFinalParis():

    heurelocal = datetime.datetime.now()
    heurelocal1 = heurelocal.strftime('%H:%M:%S')
    date1 = date.strftime('%d %B %Y')

    labeldatejour = Label(Fenetre, text=date1,
                          background="Black", fg='White', font=TailleHeure)
    labeldatejour.place(relx=0.19, rely=0.1)

    labeltextheurelocal = Label(Fenetre, text="Paris".upper(),
                                background='Black', fg='White', font=StyleEcriture)
    labeltextheurelocal.place(relx=0.1, rely=0.24)
    labelheurelocal = Label(Fenetre, text=heurelocal1.upper(),
                            background="Black", fg="White", font=Taille)
    labelheurelocal.place(relx=0.1, rely=0.3)

    Fenetre.after(1000, HeureFinalParis)

# Fonction pour l'heure de New York


def HeureFinalNewYork():

    date_actuelle = datetime.datetime.now()
    NewYork = pytz.timezone('America/New_York')
    HeureNewYork = date_actuelle.astimezone(NewYork)
    HeureNewYork1 = HeureNewYork.strftime('%H:%M:%S')

    labeltextNewYork = Label(Fenetre, text="New York".upper(),
                             background="Black", fg="White", font=StyleEcriture)
    labeltextNewYork.place(relx=0.1, rely=0.44)
    labelNewYork = Label(Fenetre, text=HeureNewYork1.upper(),
                         background='Black', fg='White', font=Taille)
    labelNewYork.place(relx=0.1, rely=0.5)
    Fenetre.after(1000, HeureFinalNewYork)

# Fonction pour l'heure de Bangkok


def HeureFinalBangkok():

    date_actuelle = datetime.datetime.now()
    Bangkok = pytz.timezone('Asia/Bangkok')
    HeureBangkok = date_actuelle.astimezone(Bangkok)
    HeureBangkok1 = HeureBangkok.strftime('%H:%M:%S')

    labeltextBangkok = Label(Fenetre, text="Bangkok".upper(),
                             background="Black", fg="White", font=StyleEcriture)
    labeltextBangkok.place(relx=0.1, rely=0.64)
    labelBangkok = Label(Fenetre, text=HeureBangkok1.upper(),
                         background='Black', fg='White', font=Taille)
    labelBangkok.place(relx=0.1, rely=0.7)
    Fenetre.after(1000, HeureFinalBangkok)


HeureFinalNewYork()
HeureFinalBangkok()
HeureFinalParis()

Fenetre.mainloop()
