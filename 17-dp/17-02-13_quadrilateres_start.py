# Exo 13-11-03 : les quadrilatères
from inspect import getmembers
from types import FunctionType

def dump(obj, title=""):
    """ imprime tous les attributs publics
        https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a
    """
    disallowed_names = {
        name for name, value in getmembers(type(obj))
        if isinstance(value, FunctionType)
    }
    attr_l =  {
        name: getattr(obj, name) for name in dir(obj)
        if name[0] != '_' and name != "factory" and  name not in disallowed_names and hasattr(obj, name)
    }
    print()
    print(title)
    for k in attr_l:
        print(k, ":", attr_l[k])


class Quadrilatere:
    quatre_cotes = True

    @classmethod
    def factory(cls,  side_l ):
        if side_l[0]==side_l[1] and side_l[0]==side_l[2] and side_l[0]==side_l[3] :
            return Losange()
        elif side_l[0]==side_l[2] and side_l[1]==side_l[3] :
            return Parallelogramme()
        else :
            return Quadrilatere()


class Trapeze(Quadrilatere):
    deux_cotes_paralleles = True


class Parallelogramme(Trapeze):
    deux_autres_cotes_paralleles = True


class Losange(Parallelogramme):
    quatre_cotes_egaux = True


class Rectangle(Parallelogramme):
    quatre_angles_droits = True


class Carre(Losange, Rectangle):
    pass

if __name__ == '__main__':
    shape1 = Quadrilatere.factory([10, 15, 20, 25])
    dump(shape1, "*** shape1")  # quadrilatère
    shape2 = Quadrilatere.factory([5, 5, 5, 5])
    dump(shape2, "*** shape2")  # losange
    shape3 = Quadrilatere.factory([5, 15, 5, 15])
    dump(shape3, "*** shape3")  # parallélogramme

    forme1 = Trapeze()
    dump(forme1, "*** Trapèze")

    forme2 = Carre()
    dump(forme2, "*** Carré")

    forme3 = Rectangle()
    dump(forme3, "*** Rectangle")

    forme4 = Losange()
    dump( forme4, "*** Losange")