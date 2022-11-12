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


def CreationFenetre():
    Fenetre = tk.Tk()
    Fenetre.geometry("800x400")
    Fenetre.title("Horaire des pays")
    Fenetre.configure(bg="grey")
    Fenetre.resizable(width=False, height=False)


def TexteInput():
    InsertionText = Label(CreationFenetre, text="Texte : ", fg='White')
    InsertionText.place(relx=0.2, rely=0.05)


CreationFenetre()
mainloop()
