
class Compte:
    __taux_interet = 0.02

    @classmethod
    def taux_interet(cls):
        return cls.__taux_interet

    @classmethod
    def taux_interet(cls, val):
        cls.__taux_interet = val

    def __init__(self, titulaire):
        self.titulaire = titulaire
        self.solde = 0
        # self.taux_interet = 0.02

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

    @solde.setter
    def solde(self, val ):
        if val < 0:
            print( 'solde insuffisant' )
            return
        self.__solde = val

    def deposer(self, montant):
        self.solde += montant
        return 'dépôt accepté'

    def retirer(self, montant):
        # if montant > self.__solde:
        #     return 'solde insuffisant'
        self.solde -= montant
        return 'retrait accepté'



if __name__ == "__main__":
    pass
