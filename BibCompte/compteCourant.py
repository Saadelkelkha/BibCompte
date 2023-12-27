from BibCompte import compte
import json

class CompteCourant(compte.Compte):
    # Inherits from the 'compte.Compte' class

    def __init__(self, proprietaire, solde, montantdecouvert):
        # Calls the constructor of the parent class
        super().__init__(proprietaire, solde)
        self.__montantdecouvert = montantdecouvert

        # Updating the 'Taux interet' field in the JSON file
        with open("data.json", "r") as file:
            data = json.load(file)
            data["Taux interet"] = self.__montantdecouvert

        # Writing the updated data back to the JSON file
        with open("data.json", "w") as file:
            json.dump(data, file, indent=2)
            file.close()
    
    @property
    def Getmontantdecouvert(self):
        return self.__montantdecouvert
    
    def __str__(self):
        # Overrides the __str__ method to include overdraft information
        return super().__str__(), f"avec un montant Decouvert autorise {self.Getmontantdecouvert}"
