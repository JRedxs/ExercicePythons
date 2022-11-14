from tkinter import *
from langdetect import detect

root = Tk()
root.geometry("450x450")
root.title("Détecteur de langue")

def Take_input():
	INPUT = inputtxt.get("1.0", "end-1c")
	print(INPUT)
	if(INPUT):
		Output.insert(END, detect(INPUT))
	else:
		Output.insert(END, "Il faut entrer du texte pour que cela fonctionne ! :) ")
	
l = Label(text =" Entrer votre Phrase / mot / paragraphe ici : ")
inputtxt = Text(root, height = 10,
				width = 50,
				bg = "light yellow")

Output = Text(root, height = 10,
			width = 50,
			bg = "light cyan")

Button_Push_Text= Button(root, height = 2,
				width = 20,
				text ="Détecter la langue d'origine",
				command = lambda:Take_input(),
				)

Button_Clear_Fields = Button(root, height = 2,
				width = 20,
				text ="Clear Fields",
				command = lambda:Take_input(),
				)

l.pack()
inputtxt.pack()

Output.pack()
Button_Push_Text.pack()
# Button_Push_Text.grid(row=3)
Button_Clear_Fields.pack()
# Button_Clear_Fields.grid(row=3)

mainloop()
