from tkinter import *
from BibCompte import compte, compteCourant, compteEpargne

window = Tk()
window.title("BANK")
window.geometry('500x400')

def Creation_COMPTE():
    # Function to create a new account based on user input
    account_type = type_var.get()
    if account_type == "Epargne":
        ACCOUNT = compteEpargne.CompteEpargne(propentry.get(), soldeentry.get(), interetentry.get())
    else:
        ACCOUNT = compteCourant.CompteCourant(propentry.get(), soldeentry.get(), mdecouvertentry.get())

    nm.config(text = compte.Compte.Getnumero() + 1)

def type_selected():
    # Function to handle radio button selection for account type
    account_type = type_var.get()
    if account_type == "Epargne":
        interetentry.config(state=NORMAL)
        mdecouvertentry.config(state=DISABLED)
    else:
        interetentry.config(state=DISABLED)
        mdecouvertentry.config(state=NORMAL)

numero = Label(window, text="Numero: ")
numero.grid(row=0, column=0)

nm = Label(window,text= compte.Compte.Getnumero() + 1)
nm.grid(row=0, column=1)

prop = Label(window, text="Proprietaire: ")
prop.grid(row=1, column=0)

propentry = Entry(window)
propentry.grid(row=1, column=1)

solde = Label(window, text="Solde initial: ")
solde.grid(row=2, column=0)

soldeentry = Entry(window)
soldeentry.grid(row=2, column=1)

solde = Label(window, text="Euro")
solde.grid(row=2, column=2)

type = Label(window, text="Type: ")
type.grid(row=3, column=0)

type_var = StringVar()

type_courant = Radiobutton(window, text="Courant", variable=type_var, value="Courant", command=type_selected)
type_courant.grid(row=3, column=1)

type_epargne = Radiobutton(window, text="Epargne", variable=type_var, value="Epargne", command=type_selected)
type_epargne.grid(row=3, column=2)

interet = Label(window, text="Taux interet: ")
interet.grid(row=4, column=0)

interetentry = Entry(window)
interetentry.grid(row=4, column=1)

mdecouvert = Label(window, text="M.Decouvert: ")
mdecouvert.grid(row=5, column=0)

mdecouvertentry = Entry(window)
mdecouvertentry.grid(row=5, column=1)

button = Button(window,text=" Creation Compte",command=Creation_COMPTE)
button.grid(row=6,column=1)

window.mainloop()
