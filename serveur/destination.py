class destination:
    def __int__(self,ville1,ville2,points):
        self.ville1 = None
        self.ville2 = None
        self.points = 0

    def __repr__(self):
        return str(self.ville1) + "  <=>  " + str(self.ville2) +"  :  "+str(self.points)