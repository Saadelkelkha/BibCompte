from datetime import datetime
import json

class Compte:
    # Class variable to track the account number
    numero = 0

    def __init__(self, proprietaire, solde):
        # Incrementing account number on each instance creation
        Compte.numero += 1
        self.__proprietaire = proprietaire
        self.__solde = solde
        # Recording the account creation date and time
        Compte.date = datetime.now()

        # Creating a dictionary to store account data
        data = {
            "Numéro": Compte.numero,
            "Propriétaire": self.__proprietaire,
            "SoldeIntial": self.__solde,
            "Taux interet": "",
            "Montant Decouvert": ""
        }

        # Appending data to a JSON file for record-keeping
        with open("data.json", "a") as file:
            json.dump(data, file, indent=2)
            file.close()

    @classmethod
    def Getnumero(cls):
        return Compte.numero

    @property
    def Getproprietaire(self):
        return self.__proprietaire

    @property
    def Getsolde(self):
        return self.__solde

    @classmethod
    def Getdate(cls):
        return Compte.date

    def __str__(self):
        # Formatting account information for display
        return "Compte de {} (n°{}) avec un solde de {} euros et ouvert le {}".format(
            self.Getproprietaire, self.Getnumero, self.Getsolde, self.Getdate)
