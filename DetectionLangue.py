#############################################################
#                                                           #
#                   VANDEVELDE ENZO                         #
#                      12-11-2022                           #
#                                                           #
#############################################################
from tkinter import *
import tkinter as tk


Fenetre = tk.Tk()
Fenetre.geometry("900x500")
Fenetre.title("Horaire des pays")
Fenetre.configure(bg="grey")
Fenetre.resizable(width=False, height=False)


def TexteInput():
    InsertionText = Label(Fenetre, text="Texte : ", bg='grey', fg='White')
    InsertionText.place(relx=0.063, rely=0.05)
    Canvas(Fenetre, width=770, height=100, bg='White',
           borderwidth=2, relief='solid').pack(padx=0.3, pady=70)


TexteInput()
mainloop()
