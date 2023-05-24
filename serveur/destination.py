class Destination:
    def __init__(self, villeA, villeB, points, id, villeC=None):
        self.id = id
        self.ville1 = villeA
        self.ville2 = villeB
        self.ville3 = villeC
        self.points = points

    def __repr__(self):
        if self.ville3 is None:
            return str(self.ville1) + "  <=>  " + str(self.ville2) + "  :  " + str(self.points)
        else:
            return str(self.ville1) + "  <=>  " + str(self.ville2) + "  <=>  " + str(self.ville3) + "  :  " + str(
                self.points)