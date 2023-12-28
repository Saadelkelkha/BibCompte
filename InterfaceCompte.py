from tkinter import *
from BibCompte import compte, compteCourant, compteEpargne
import json

window = Tk()
window.title("BANK")
# window.geometry('500x400')

def Creation_COMPTE():
    # Function to create a new account based on user input
    account_type = type_var.get()
    if account_type == "Epargne":
        ACCOUNT = compteEpargne.CompteEpargne(propentry.get(), soldeentry.get(), interetentry.get())

        with open("data.json", "r") as file:
            date = json.load(file)
            date["compte"].append({
            "Numero": compte.Compte.Getnumero() ,
            "Proprietaire": propentry.get(),
            "SoldeIntial": soldeentry.get(),
            "Taux interet": interetentry.get(),
            "Montant Decouvert": ""
        })
            file.close()
    else:
        ACCOUNT = compteCourant.CompteCourant(propentry.get(), soldeentry.get(), mdecouvertentry.get())

        with open("data.json", "r") as file:
            date = json.load(file)
            date["compte"].append({
            "Numero": compte.Compte.Getnumero() ,
            "Proprietaire": propentry.get(),
            "SoldeIntial": soldeentry.get(),
            "Taux interet": "",
            "Montant Decouvert": mdecouvertentry.get()
        })
    with open("data.json", "w") as file:
        json.dump(date, file, indent=2)

    nm.config(text = compte.Compte.Getnumero() + 1)
    with open("data.json", "r") as file :
        data = json.load(file)

    for i in range(0, len(data["compte"])): 
        for j in range(width):   
            if j == 0 :
                b = Entry(window)
                b.grid(row=i+7, column=j)
                b.insert(END, "")
            if j == 1 :
                b = Entry(window)
                b.grid(row=i+7, column=j)
                b.insert(END, data["compte"][i]["Numero"] )
            if j == 2 :
                b = Entry(window)
                b.grid(row=i+7, column=j)
                b.insert(END, data["compte"][i]["Proprietaire"] )
            if j == 3 :
                b = Entry(window)
                b.grid(row=i+7, column=j)
                b.insert(END, data["compte"][i]["SoldeIntial"])

            if j == 4 :
                b = Entry(window)
                b.grid(row=i+7, column=j)
                b.insert(END, data["compte"][i]["Taux interet"])

            if j == 5 :
                b = Entry(window)
                b.grid(row=i+7, column=j)
                b.insert(END, data["compte"][i]["Montant Decouvert"])
    
        
    

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

height = compte.Compte.Getnumero() 
width = 6

with open("data.json", "r") as file :
        data = json.load(file)

for i in range(0, len(data["compte"])): 
        for j in range(width):   
            if j == 0 :
                b = Entry(window)
                b.grid(row=i+7, column=j)
                b.insert(END, "")
            if j == 1 :
                b = Entry(window)
                b.grid(row=i+7, column=j)
                b.insert(END, data["compte"][i]["Numero"] )
            if j == 2 :
                b = Entry(window)
                b.grid(row=i+7, column=j)
                b.insert(END, data["compte"][i]["Proprietaire"] )
            if j == 3 :
                b = Entry(window)
                b.grid(row=i+7, column=j)
                b.insert(END, data["compte"][i]["SoldeIntial"])

            if j == 4 :
                b = Entry(window)
                b.grid(row=i+7, column=j)
                b.insert(END, data["compte"][i]["Taux interet"])

            if j == 5 :
                b = Entry(window)
                b.grid(row=i+7, column=j)
                b.insert(END, data["compte"][i]["Montant Decouvert"])

window.mainloop()