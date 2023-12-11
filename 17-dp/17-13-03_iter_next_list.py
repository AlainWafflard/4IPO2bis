

nom_l = [ "ALbert", "Bernard", "Carine" ]
gen_nom_l = iter(nom_l)

while True :
    try:
        val = next(gen_nom_l)
        print(val)
    except StopIteration:
        print("fin de liste")
        break

