class Stock:

    def __init__(self, crayon=0, papier=0):
        self.__seuil_papier = 0
        self.__seuil_crayon = 0
        self.crayon = crayon
        self.papier = papier

    def __str__(self):
        return f"""
            stock de papier : {self.papier}
            stock de crayon : {self.crayon}
        """

    @property
    def papier(self):
        return self.__papier

    @papier.setter
    def papier(self, val):
        if val >= 0 :
            self.__papier = val
        else:
            self.__papier = 0
            print("papier = 0")
        # self.__check_stock()
        # on checke la recommande
        if self.__papier <= self.__seuil_papier :
            print("recommander papier")


    @property
    def crayon(self):
        return self.__crayon

    @crayon.setter
    def crayon(self, val):
        if val >= 0 :
            self.__crayon = val
        else:
            self.__crayon = 0
            print("crayon = 0")
        # self.__check_stock()
        if self.__crayon <= self.__seuil_crayon :
            print("recommander crayon")

    def seuil_de_recommande(self, crayon=0, papier=0):
        self.__seuil_papier = papier
        self.__seuil_crayon = crayon

    # def __check_stock(self):
    #     """
    #     compare les stocks avec les seuils de recommande
    #     imprime un message en cas de recommande nécessaire
    #     """
    #     if self.papier <= self.__seuil_papier :
    #         print("recommander papier")
    #     if self.crayon <= self.__seuil_crayon :
    #         print("recommander crayon")

    def retirer(self, crayon=0, papier=0):
        if  papier > 0 :
            if self.papier < papier:
                print(f"pas assez de papier; vous recevez {self.papier}")
                self.papier = 0
            else:
                print(f"il y a assez de papier; vous recevez {papier}")
                self.papier -= papier
        if crayon > 0 :
            if self.crayon < crayon:
                print(f"pas assez de crayon; vous recevez {self.crayon}")
                self.crayon = 0
            else:
                print(f"il y a assez de crayon; vous recevez {crayon}")
                self.crayon -= crayon
        # self.__check_stock()

    # def valeur(self):
    #     self.__check_stock()


if __name__ == "__main__":
    stock = Stock(papier=20,crayon=8)
    stock.seuil_de_recommande(papier=2, crayon=1)
    print(stock)  # imprime état du stock – tout va bien
    stock.retirer(papier=12, crayon=6)
    print(stock)
    stock.retirer(papier=7)  # message de recommande
    print(stock)
    stock.retirer(crayon=3)  # message de recommande
    print(stock)
    # stock.valeur()  # message de recommande
    # print(stock)

