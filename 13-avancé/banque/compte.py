class Compte:

    def __init__(self, titulaire):
        self.__titulaire = titulaire
        self.__solde = 0

    def __del__(self):
        print(f"compte  {self.titulaire} détruit, solde {self.solde}")

    @property
    def titulaire (self):
        return self.__titulaire

    @titulaire.setter
    def titulaire(self, name):
        # tests de validité ...
        self.__titulaire = name

    @property
    def solde(self):
        return self.__solde

    def deposer(self, montant):
        self.__solde += montant
        return 'dépôt accepté'

    def retirer(self, montant):
        if montant > self.__solde:
            return 'solde insuffisant'
        self.__solde -= montant
        return 'retrait accepté'


if __name__ == "__main__":
    c_kim = Compte('Kim')
    c_kim.deposer(100)
    print(c_kim.solde)

