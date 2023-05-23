from constantes import *
from chemin import Chemin
class Plateau:
    def __init__(self):
        self.liste_chemin = [
            Chemin(VERT,   5, 0,  TYPE_WAGON,  (30, 33, 0)),
            Chemin(NOIR,   5, 1,  TYPE_WAGON,  (1,  2,  0)),
            Chemin(JAUNE,  4, 2,  TYPE_BATEAU, (1,  2,  1)),
            Chemin(VIOLET, 5, 3,  TYPE_BATEAU, (2,  36, 0)),
            Chemin(NOIR,   5, 4,  TYPE_BATEAU, (2,  36, 1)),
            Chemin(GRIS,   1, 5,  TYPE_BATEAU, (1,  36, 0)),
            Chemin(GRIS,   1, 6,  TYPE_BATEAU, (1,  36, 1)),
            Chemin(VIOLET, 3, 7,  TYPE_BATEAU, (1,  3)),
            Chemin(JAUNE,  3, 8,  TYPE_BATEAU, (2,  6)),
            Chemin(VERT,   4, 9,  TYPE_WAGON,  (2, 5)),
            Chemin(GRIS,   2, 10, TYPE_WAGON,  (5, 6)),
            Chemin(BLANC,  4, 11, TYPE_WAGON,  (6, 7)),
            Chemin(VIOLET, 5, 12, TYPE_WAGON,  (6, 8)),
            Chemin(VERT,   3, 13, TYPE_WAGON,  (7, 8)),
            Chemin(JAUNE,  5, 14, TYPE_WAGON,  (8, 9, 0)),
            Chemin(ROUGE,  5, 15, TYPE_WAGON,  (8, 9, 1)),
            Chemin(GRIS,   3, 16, TYPE_WAGON,  (7, 8)), 
            Chemin(GRIS,   1, 17, TYPE_WAGON,  (7, 12))

        ]

    def ville_relier(self, id_joueur):
        """
        calcule si deux ville sont relier par le joueur d'id id_joueur

        :return:
        """



