class Point:

    def __init__(self, coord=(0, 0) ):
        self.coord = coord
        self._distance = None

    def __del__(self):
        print("point détruit")

    def __str__(self):
        return f" abscisse {self.coord[0]}, ordonnée {self.coord[1]} "

    def distance(self):
        if self._distance is None:
            print("distance calculée")
            self._distance = self.coord[0] + self.coord[1]
        return self._distance

    def abscisse(self):
        return self.coord[0]

    def ordonnee(self):
        return self.coord[1]
