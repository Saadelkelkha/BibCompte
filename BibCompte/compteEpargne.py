from BibCompte import compte
import json

class CompteEpargne(compte.Compte):
    # Inherits from the 'compte.Compte' class

    def __init__(self, proprietaire, solde, interet):
        # Calls the constructor of the parent class
        super().__init__(proprietaire, solde)
        self.__interet = interet

        # Reading existing data from the JSON file
        with open("data.json", "r") as file:
            data = json.load(file)
            data["Taux interet"] = self.__interet

        # Writing the updated data back to the JSON file
        with open("data.json", "w") as file:
            json.dump(data, file, indent=2)
            file.close()

    @property
    def Getinteret(self):
        return self.__interet
    
    def __str__(self):
        # Overrides the __str__ method to include interest rate information
        return super().__str__(), f"avec un taux interet {self.Getinteret}"
