class Rectangle:
    def __init__(self, long, larg):
        self.long = long
        self.larg = larg

    def __str__(self):
        return f"Rectangle {self.long} {self.larg}"

    def __add__(self,  other):
        if self.larg != other.larg :
            print("largeurs non identiques")
            return None
        return Rectangle( self.long+other.long, self.larg)


if __name__ == "__main__":
    r1 = Rectangle( 8, 2 )
    r2 = Rectangle( 6, 3 )
    rtot = r1 + r2
    print(r1, r2, rtot)

