class Date:

    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def __str__(self):
        return f"{self.annee}-{self.mois}-{self.jour}"

    def __lt__(self, other):
        if self.annee != other.annee :
            return self.annee < other.annee
        elif self.mois != other.mois :
            return self.mois < other.mois
        else:
            return self.jour < other.jour


d1 = Date(5, 3, 1990)
d2 = Date(10, 3, 1990)
d3 = Date(8, 5, 1980)

# print( d1 < d2 )
# print( d1 >= d2 )
my_list = [ d1, d2, d3 ]
for o in my_list : print(o)
print()
my_sorted_list = sorted(my_list)
for o in my_sorted_list : print(o)

# print(my_list)

