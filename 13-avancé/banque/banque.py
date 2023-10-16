import compte

class Banque :

    def __init__(self, name):
        self.name = name
        self.compte_d = {}

    def __del__(self):
        print(f"banque {self.name} détruite")
    def __str__(self):
        s = f"banque {self.name}\n"
        for c in self.compte_d.values():
            s += f"compte {c.titulaire}\n"
        return s

    def ajouter_compte(self, titulaire):
        c = compte.Compte(titulaire)
        # self.compte_d.append(c)
        self.compte_d[titulaire] = c

    def deposer_argent(self, titu, montant):
        self.compte_d[titu].deposer(montant)


if __name__ == '__main__':
    b = Banque("Belfius")
    b.ajouter_compte("Kim")
    # b.compte_d["Kim"].deposer(100)
    b.ajouter_compte("Sandra")
    b.deposer_argent("Sandra",200)
    print(b)
    b = None
    print("------------")
