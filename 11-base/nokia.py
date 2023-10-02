def change_marque(myobj):
    myobj.marque = "Sony"

class NokiaPhone:
    marque = "Nokia"
    id = 1

    def __init__(self, name, serie, poids):
        """  constructeur """
        #self.marque = "Nokia"
        self.identifier = name
        self.serie = serie
        self.poids = poids
        self.id = NokiaPhone.id
        NokiaPhone.id += 1
        print("objet créé")

    def __del__(self):
        """ destructeur """
        print(f"objet de {self.identifier} détruit")

    def print_specs(self):
        app = "téléphone"
        print(f"ceci est le {app} de {self.identifier}")

    def __brol__(self):
        pass

    def __str__(self):
        return f"""
smartphone de {self.identifier}
marque : {self.marque}
serie : {self.serie}
poids : {self.poids}
id : {self.id}
"""

    def __repr__(self):
        return f"{self.identifier};{self.marque}"



# user = input("utilisateur ?")
# age = int(input("son âge ? "))
# age = str(age)
# print( age_s )

# mysmartphone = NokiaPhone()
# mysmartphone.init("Kim", 5110, 199)


smartphone_l = []
smartphone_l.append(NokiaPhone("Kim", 5110, 199))
smartphone_l.append(NokiaPhone("Tom", 6220, 250))
nokia_ann = NokiaPhone("Ann", 6220, 250)

for sm in smartphone_l:
    change_marque(sm)
    print(sm)

for sm in smartphone_l:
    print(repr(sm))

sm1 = NokiaPhone("Tom", 6220, 250)
sm2 = NokiaPhone("Tom", 6220, 250)
sm3 = sm2
print( sm1 is sm2 )
