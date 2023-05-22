from constantes import *
from chemin import Chemin
class Plateau:
    def __int__(self):
        self.liste_chemin = [
            Chemin(NOIR, 5, 1, TYPE_WAGON,(1,2))
        ]

    def ville_relier(self, id_joueur):
        """
        calcule si deux ville sont relier par le joueur d'id id_joueur

        :return:
        """



