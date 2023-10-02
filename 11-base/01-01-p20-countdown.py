# Affiche un compte à rebours.
# Décompte à partir de 5.
# Charles Pecheur 5 septembre 2018

i = 5 # valeur de départ du décompte
myvar = False

while i >= 0 and not myvar:
    if i != 0:
        print(i , "|")
    else:
        print("Decollage" + "maintenant", sep="-")
    i -= 1

print()
print("Reussi")

myvar = False
if not myvar:
    print("gnagna")

my_sytring = """
abc sdfs    qdf sqdf
er  ezrt    zer er
"""
print(my_sytring)
