# Programmez un feu de
# signalisation
# • classe Light
# • trois états : 1 rouge / 2 vert / 3 orange
# • pas d'aspect graphique
# Output:
# light color is 1
# light color is 2
# light color is 3
# light color is 1

class Light:

    def __init__(self, name="default", color=1):
        self.name = name
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, val):
        if val not in ( 1, 2, 3):
            val = 1
        self.__color = val

    def change(self):
        """
        change l'état du feu
        1 --> 2 --> 3 --> 1  etc.
        """
        self.color += 1
        # if self.color > 3 :
        #     self.color = 1

    def __str__(self):
        # return f"light color is {self.color}"
        return f"{self.color}"


feu01 = Light( "Buedts", 1 )
print(str(feu01.color))
feu01.change()
print(str(feu01.color))
feu01.change()
print(str(feu01.color))
feu01.change()
print(str(feu01.color))
feu01.change()
print(str(feu01.color))
feu01.change()
print(str(feu01.color))
feu01.change()
print(str(feu01.color))


# feu01 = Light("buedts")
# for i in range(50):
#     print(feu01, end=" ")
#     feu01.change()
#     if (i+1) % 10 == 0 :
#         print()
#
# feu02 = Light("chasse", 3)
# print(feu02)
