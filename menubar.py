from tkinter import *
import tkinter as tk

app = tk.Tk() 
app.geometry('300x200')
app.title("Basic Menu Bar")

menubar = tk.Menu(app)

menufichier = Menu(menubar, tearoff=0,relief='flat', bd=5,activebackground='red',activeborderwidth=1, font=("Verdana", 12))
menubar.add_cascade(label="Fichier", menu=menufichier)
menufichier.add_command(label="Ouvrir ")
menufichier.add_command(label="Enregistrer")
menufichier.add_command(label="Quitter")

Client1= Menu(menubar, tearoff=0,relief='flat', bd=5,activebackground='red',activeborderwidth=1, font=("Verdana", 12))
menubar.add_cascade(label="Client1", menu=Client1)
Client1_Trier = Menu(menubar, tearoff=0)
Client1_Trier.add_command(label="RAM")
Client1_Trier.add_command(label="SWAP")
Client1.add_cascade(label="trier", underline=0, menu=Client1_Trier)

Client1_graphiques = Menu(menubar, tearoff=0)
Client1_graphiques.add_command(label="RAM")
Client1_graphiques.add_command(label="SWAP")
Client1.add_cascade(label="Graphiques", underline=0, menu=Client1_graphiques)


Client2= Menu(menubar, tearoff=0,relief='flat', bd=5,activebackground='red',activeborderwidth=1, font=("Verdana", 12))
menubar.add_cascade(label="Client2", menu=Client2)
Client2_Trier = Menu(menubar, tearoff=0)
Client2_Trier.add_command(label="RAM")
Client2_Trier.add_command(label="SWAP")
Client2.add_cascade(label="Trier", underline=0, menu=Client2_Trier)

Client2_graphiques = Menu(menubar, tearoff=0)
Client2_graphiques.add_command(label="RAM")
Client2_graphiques.add_command(label="SWAP")
Client2.add_cascade(label="Graphiques", underline=0, menu=Client2_graphiques)

app.config(menu=menubar)
app.mainloop()

