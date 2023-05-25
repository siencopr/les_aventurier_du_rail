from constantes import *
from chemin import Chemin

class Plateau:
    def __init__(self):
        self.relier = {}
        self.liste_chemin = [
            Chemin(VERT__, 5,  0, TYPE_WAGON_, (30, 33, 0)),
            Chemin(NOIR__, 5,  1, TYPE_WAGON_, (1, 2, 0)),
            Chemin(JAUNE_, 4,  2, TYPE_BATEAU, (1, 2, 1)),
            Chemin(VIOLET, 5,  3, TYPE_BATEAU, (2, 36, 0)),
            Chemin(NOIR__, 5,  4, TYPE_BATEAU, (2, 36, 1)),
            Chemin(GRIS__, 1,  5, TYPE_BATEAU, (1, 36, 0)),
            Chemin(GRIS__, 1,  6, TYPE_BATEAU, (1, 36, 1)),
            Chemin(VIOLET, 3,  7, TYPE_BATEAU, (1, 3)),
            Chemin(JAUNE_, 3,  8, TYPE_BATEAU, (2, 6)),
            Chemin(VERT__, 4,  9, TYPE_WAGON_, (2, 5)),
            Chemin(GRIS__, 2, 10, TYPE_WAGON_, (5, 6)),
            Chemin(BLANC_, 4, 11, TYPE_WAGON_, (6, 7)),
            Chemin(VIOLET, 5, 12, TYPE_WAGON_, (6, 8)),
            Chemin(VERT__, 3, 13, TYPE_WAGON_, (7, 8)),
            Chemin(JAUNE_, 5, 14, TYPE_WAGON_, (8, 9, 0)),
            Chemin(ROUGE_, 5, 15, TYPE_WAGON_, (8, 9, 1)),
            Chemin(GRIS__, 3, 16, TYPE_WAGON_, (7, 8)),
            Chemin(GRIS__, 1, 17, TYPE_WAGON_, (7, 12))

            Chemin(VIOLET, 5, 18, TYPE_WAGON_, (8, 9, 0)),
            Chemin(NOIR__, 5, 19, TYPE_WAGON_, (8, 9, 1)),
            Chemin(BLANC_, 3, 20, TYPE_WAGON_, (7, 8)),
            Chemin(ROUGE_, 1, 21, TYPE_WAGON_, (7, 12))
            Chemin(BLANC_, 5, 22, TYPE_WAGON_, (30, 33, 0)),
            Chemin(VERT__, 5, 23, TYPE_WAGON_, (1, 2, 0)),
            Chemin(ROUGE_, 4, 24, TYPE_BATEAU, (1, 2, 1)),
            Chemin(VIOLET, 5, 25, TYPE_BATEAU, (2, 36, 0)),
            Chemin(NOIR__, 5, 26, TYPE_BATEAU, (2, 36, 1)),
            Chemin(GRIS__, 1, 27, TYPE_BATEAU, (1, 36, 0)),
            Chemin(GRIS__, 1, 28, TYPE_BATEAU, (1, 36, 1)),
            Chemin(VIOLET, 3, 29, TYPE_BATEAU, (1, 3)),
            Chemin(JAUNE_, 3, 30, TYPE_BATEAU, (2, 6)),
            Chemin(VERT__, 4, 31, TYPE_WAGON_, (2, 5)),
            Chemin(GRIS__, 2, 32, TYPE_WAGON_, (5, 6)),
            Chemin(BLANC_, 4, 33, TYPE_WAGON_, (6, 7)),
            Chemin(VIOLET, 5, 34, TYPE_WAGON_, (6, 8)),
            Chemin(VERT__, 3, 35, TYPE_WAGON_, (7, 8)),
            Chemin(JAUNE_, 5, 36, TYPE_WAGON_, (8, 9, 0)),
            Chemin(ROUGE_, 5, 37, TYPE_WAGON_, (8, 9, 1)),
            Chemin(GRIS__, 3, 38, TYPE_WAGON_, (7, 8)),
            Chemin(GRIS__, 1, 39, TYPE_WAGON_, (7, 12))
            Chemin(VIOLET, 5, 40, TYPE_WAGON_, (8, 9, 0)),
            Chemin(NOIR__, 5, 41, TYPE_WAGON_, (8, 9, 1)),
            Chemin(BLANC_, 3, 42, TYPE_WAGON_, (7, 8)),
            Chemin(ROUGE_, 1, 43, TYPE_WAGON_, (7, 12))
            Chemin(BLANC_, 5, 44, TYPE_WAGON_, (30, 33, 0)),
            Chemin(VERT__, 5, 45, TYPE_WAGON_, (1, 2, 0)),
            Chemin(ROUGE_, 4, 46, TYPE_BATEAU, (1, 2, 1)),
            Chemin(VIOLET, 5, 47, TYPE_BATEAU, (2, 36, 0)),
            Chemin(NOIR__, 5, 48, TYPE_BATEAU, (2, 36, 1)),
            Chemin(GRIS__, 1, 49, TYPE_BATEAU, (1, 36, 0)),
            Chemin(GRIS__, 1, 50, TYPE_BATEAU, (1, 36, 1)),
            Chemin(VIOLET, 3, 51, TYPE_BATEAU, (1, 3)),
            Chemin(JAUNE_, 3, 52, TYPE_BATEAU, (2, 6)),
            Chemin(VERT__, 4, 53, TYPE_WAGON_, (2, 5)),
            Chemin(GRIS__, 2, 54, TYPE_WAGON_, (5, 6)),
            Chemin(BLANC_, 4, 55, TYPE_WAGON_, (6, 7)),
            Chemin(VIOLET, 5, 56, TYPE_WAGON_, (6, 8)),

            Chemin(VERT__, 3, 57, TYPE_WAGON_, (7, 8)),
            Chemin(JAUNE_, 5, 58, TYPE_WAGON_, (8, 9, 0)),
            Chemin(ROUGE_, 5, 59, TYPE_WAGON_, (8, 9, 1)),
            Chemin(GRIS__, 3, 60, TYPE_WAGON_, (7, 8)),
            Chemin(GRIS__, 1, 61, TYPE_WAGON_, (7, 12))

        ]

    def ville_relier(self, id_joueur, num_ville, origine = None):
        """
        calcule si deux ville sont relier par le joueur d'id id_joueur

        :return:
        """

        if origine is None:
            origine = num_ville
        if not self.relier.get(origine):
            self.relier[origine] = []

        ligne_local = Matrice.matrice_plateau[num_ville]


        for i in range(len(ligne_local)):
            if i in self.relier[origine]:
                pass
            elif ligne_local[i] == id_joueur:
                self.relier[origine].append(i)
                self.ville_relier(id_joueur, i, origine)
            elif type(ligne_local[i]) == list:
                if id_joueur in ligne_local[i]:
                    self.relier[origine].append(i)
                    self.ville_relier(id_joueur, i, origine)

        return self.relier[origine]

    def reliee(self, villeA, villeB, id_joueur):
        """
        calcule si deux villes sont relier par le joueur id_joueur

        :param villeA:
        :param villeB:
        :param id_joueur:
        :return:
        """
        return villeA in self.ville_relier(id_joueur, villeB)