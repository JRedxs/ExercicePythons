#############################################################
#                                                           #
#                   VANDEVELDE ENZO                         #
#                   RYCKEBUSCH REMI                         #
#                      12-11-2022                           #
#                                                           #
#                                                           #
#                                                           #
#############################################################


from tkinter import *
from langdetect import detect





root = Tk()
root.geometry("640x550")
root.title("Détecteur de langue")

def Take_input():
	INPUT = inputtxt.get("1.0", "end-1c")
	print(" Vous avez entre : " ,INPUT, " - La langue detectee est : ", detect(INPUT))
	if(INPUT):
		Output.insert(END, detect(INPUT))
	else:
		Output.insert(END, "Il faut entrer du texte pour que cela fonctionne ! :) ")

def delete():
		inputtxt.delete("1.0",'end')
		Output.delete("1.0",'end')

	
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
				command = delete,
				)

l.pack()
inputtxt.pack(pady=10, padx=5)

Output.pack(pady=10, padx=5)
Button_Push_Text.pack(pady=10, padx= 5,
)
# Button_Push_Text.grid(row=3)
Button_Clear_Fields.pack(pady=10, padx=5)
# Button_Clear_Fields.grid(row=3)

mainloop()
