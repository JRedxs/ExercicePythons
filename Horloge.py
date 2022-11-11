from tkinter import *
import tkinter as tk
import datetime
import locale
locale.setlocale(locale.LC_TIME, '')

Fenetre = tk.Tk()
Fenetre.geometry("300x500")
Fenetre.title("Horaire des pays")
Fenetre.configure(bg="black")
Fenetre.resizable(width=False, height=False)

date = datetime.date.today()
day = datetime.date.today()
day1 = day.strftime('%A')


labelday = Label(Fenetre, text=day1.upper(), background="Black", fg='White')
labelday.place(relx=0.1, rely=0.02)

labeldatejour = Label(Fenetre, text=date, background="Black", fg='White')
labeldatejour.place(relx=0.1, rely=0.06)


Fenetre.mainloop()
