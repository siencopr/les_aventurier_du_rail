class file:
    def __int__(self):
        self.contenue = []

    def est_vide(self):
        return self.contenue == []
    def enfiller_liste(self, liste):
        for elm in liste:
                self.contenue.append(elm)

    def deffiler(self):
        return self.contenue.pop(0)