from constantes import *
from chemin import Chemin
from comunication import *
Comu = Communication()

class Plateau:
    def __init__(self):
        self.relier = {}
        self.liste_chemin = [
            Chemin(VERT__, 5,  0, TYPE_WAGON_, (30, 33, 0)),
            Chemin(NOIR__, 5,  1, TYPE_WAGON_, (1, 2, 0)),
            Chemin(JAUNE_, 4,  2, TYPE_BATEAU, (1, 2, 1)),
            Chemin(VIOLET, 5,  3, TYPE_BATEAU, (2, 0, 0)),
            Chemin(NOIR__, 5,  4, TYPE_BATEAU, (2, 0, 1)),
            Chemin(GRIS__, 1,  5, TYPE_BATEAU, (1, 0, 0)),
            Chemin(GRIS__, 1,  6, TYPE_BATEAU, (1, 0, 1)),
            Chemin(VIOLET, 3,  7, TYPE_BATEAU, (1, 3)),
            Chemin(JAUNE_, 3,  8, TYPE_WAGON_, (2, 6)),
            Chemin(VERT__, 4,  9, TYPE_WAGON_, (2, 5)),
            Chemin(GRIS__, 2, 10, TYPE_WAGON_, (5, 6)),
            Chemin(BLANC_, 4, 11, TYPE_WAGON_, (6, 7)),
            Chemin(VIOLET, 5, 12, TYPE_WAGON_, (6, 8)),
            Chemin(VERT__, 3, 13, TYPE_WAGON_, (7, 8)),
            Chemin(JAUNE_, 5, 14, TYPE_WAGON_, (8, 9, 0)),
            Chemin(ROUGE_, 5, 15, TYPE_WAGON_, (8, 9, 1)),
            Chemin(GRIS__, 3, 16, TYPE_WAGON_, (7, 9)),
            Chemin(GRIS__, 1, 17, TYPE_WAGON_, (7, 12)),
            Chemin(VIOLET, 4, 18, TYPE_WAGON_, (5, 7)),
            Chemin(NOIR__, 4, 19, TYPE_WAGON_, (5, 12)),
            Chemin(BLANC_, 4, 20, TYPE_WAGON_, (4, 5)),
            Chemin(ROUGE_, 6, 21, TYPE_BATEAU, (2, 4)),
            Chemin(BLANC_, 2, 22, TYPE_BATEAU, (0, 3)),
            Chemin(VERT__, 5, 23, TYPE_BATEAU, (0,13,0)),
            Chemin(ROUGE_, 5, 24, TYPE_BATEAU, (0,13,1)),
            Chemin(GRIS__, 2, 25, TYPE_BATEAU, (0, 4)),
            Chemin(GRIS__, 4, 26, TYPE_BATEAU, (3, 13)),
            Chemin(JAUNE_, 5, 27, TYPE_WAGON_, (3, 16)),
            Chemin(VERT__, 4, 28, TYPE_WAGON_, (16,28)),
            Chemin(BLANC_, 4, 29, TYPE_WAGON_, (16,17,0)),
            Chemin(ROUGE_, 4, 30, TYPE_WAGON_, (16,17,1)),
            Chemin(GRIS__, 8, 31, TYPE_WAGON_, (28,30)),
            Chemin(ROUGE_, 7, 32, TYPE_WAGON_, (28,29)),
            Chemin(VIOLET, 4, 33, TYPE_WAGON_, (28, 17)),
            Chemin(ROUGE_, 1, 34, TYPE_WAGON_, (5,11)),
            Chemin(GRIS__, 3, 35, TYPE_BATEAU, (4, 13)),
            Chemin(GRIS__, 6, 36, TYPE_BATEAU, (11, 13, 0)),
            Chemin(GRIS__, 6, 37, TYPE_BATEAU, (11, 13, 1)),
            Chemin(VERT__, 3, 38, TYPE_BATEAU, (11, 14)),
            Chemin(JAUNE_, 3, 39, TYPE_BATEAU, (11, 12,0)),
            Chemin(NOIR__, 3, 40, TYPE_BATEAU, (11, 12, 1)),
            Chemin(GRIS__, 2, 41, TYPE_BATEAU, (12, 15)),
            Chemin(BLANC_, 1, 42, TYPE_BATEAU, (12, 9,0)),
            Chemin(VERT__, 1, 43, TYPE_BATEAU, (12, 9,1)),
            Chemin(VIOLET, 3, 44, TYPE_BATEAU, (15, 9)),
            Chemin(GRIS__, 1, 45, TYPE_WAGON_, (9, 10, 0)),
            Chemin(GRIS__, 1, 46, TYPE_WAGON_, (9,10, 1)),
            Chemin(JAUNE_, 3, 47, TYPE_WAGON_, (15, 10)),
            Chemin(NOIR__, 4, 48, TYPE_WAGON_, (20, 10)),
            Chemin(GRIS__, 3, 49, TYPE_WAGON_, (10, 21, 0)),
            Chemin(VIOLET, 3, 50, TYPE_WAGON_, (10,21, 1)),
            Chemin(GRIS__, 1, 51, TYPE_BATEAU, (20,21,0)),
            Chemin(GRIS__, 1, 52, TYPE_BATEAU, (20, 21,1)),
            Chemin(JAUNE_, 2, 53, TYPE_BATEAU, (20, 22)),
            Chemin(ROUGE_, 2, 54, TYPE_BATEAU, (21,22,0)),
            Chemin(BLANC_, 2, 55, TYPE_BATEAU, (21,22,1)),
            Chemin(ROUGE_, 3, 56, TYPE_BATEAU, (14, 15,0)),
            Chemin(BLANC_, 3, 57, TYPE_WAGON_, (14, 15,1)),
            Chemin(ROUGE_, 3, 58, TYPE_WAGON_, (14, 19)),
            Chemin(GRIS__, 3, 59, TYPE_BATEAU, (13, 14)),
            Chemin(GRIS__, 3, 60, TYPE_BATEAU, (13, 18)),
            Chemin(JAUNE_, 4, 61, TYPE_BATEAU, (13, 36,0)),
            Chemin(BLANC_, 4, 62, TYPE_BATEAU, (13, 36,1)),
            Chemin(GRIS__, 2, 63, TYPE_WAGON_, (17, 18)),
            Chemin(GRIS__, 1, 64, TYPE_BATEAU, (36,18)),
            Chemin(GRIS__, 2, 65, TYPE_BATEAU, (18, 23)),
            Chemin(BLANC_, 2, 66, TYPE_BATEAU, (18,27)),
            Chemin(GRIS__, 2, 67, TYPE_WAGON_, (17,27)),
            Chemin(NOIR__, 7, 68, TYPE_WAGON_, (17,29,0)),
            Chemin(VERT__, 7, 69, TYPE_WAGON_, (17,29,1)),
            Chemin(JAUNE_, 2, 70, TYPE_WAGON_, (29,31)),
            Chemin(GRIS__, 1, 71, TYPE_WAGON_, (29,30,0)),
            Chemin(GRIS__, 1, 72, TYPE_WAGON_, (29,30,1)),
            Chemin(JAUNE_, 3, 73, TYPE_BATEAU, (31,30,0)),
            Chemin(VERT__, 3, 74, TYPE_BATEAU, (31,30,1)),
            Chemin(GRIS__, 2, 75, TYPE_BATEAU, (36,19)),
            Chemin(VERT__, 2, 76, TYPE_WAGON_, (19,20)),
            Chemin(NOIR__, 4, 77, TYPE_BATEAU, (36,20,0)),
            Chemin(VERT__, 4, 78, TYPE_BATEAU, (36,20,1)),
            Chemin(GRIS__, 1, 79, TYPE_BATEAU, (36,23)),
            Chemin(JAUNE_, 2, 80, TYPE_BATEAU, (23,27)),
            Chemin(ROUGE_, 5, 81, TYPE_WAGON_, (20,24)),
            Chemin(BLANC_, 2, 82, TYPE_WAGON_, (23, 24)),
            Chemin(NOIR__, 2, 83, TYPE_WAGON_, (27, 24)),
            Chemin(BLANC_, 4, 84, TYPE_BATEAU, (24, 31)),
            Chemin(NOIR__, 4, 85, TYPE_BATEAU, (24, 31)),
            Chemin(GRIS__, 1, 86, TYPE_BATEAU, (24, 26, 0)),
            Chemin(GRIS__, 1, 87, TYPE_BATEAU, (24, 26, 1)),
            Chemin(VIOLET, 6, 88, TYPE_BATEAU, (20, 26, 0)),
            Chemin(BLANC_, 6, 89, TYPE_BATEAU, (20, 26, 1)),
            Chemin(NOIR__, 1, 90, TYPE_BATEAU, (22, 25, 0)),
            Chemin(VERT__, 1, 91, TYPE_BATEAU, (22, 25, 1)),
            Chemin(GRIS__, 9, 92, TYPE_WAGON_, (22, 35)),
            Chemin(VIOLET, 6, 93, TYPE_WAGON_, (25, 34,0)),
            Chemin(JAUNE_, 6, 94, TYPE_WAGON_, (25,34,1)),
            Chemin(ROUGE_, 1, 95, TYPE_WAGON_, (34, 35,0)),
            Chemin(VERT__, 1, 96, TYPE_WAGON_, (34, 35,1)),
            Chemin(GRIS__, 4, 97, TYPE_WAGON_, (26, 34)),
            Chemin(JAUNE_, 3, 98, TYPE_BATEAU, (26, 32,0)),
            Chemin(ROUGE_, 3, 99, TYPE_BATEAU, (26, 32,1)),
            Chemin(GRIS__, 4, 100, TYPE_BATEAU, (26, 31)),
            Chemin(VIOLET, 2, 101, TYPE_WAGON_, (31,32)),
            Chemin(VERT__, 2, 102, TYPE_BATEAU, (32, 33,0)),
            Chemin(VIOLET, 2, 103, TYPE_BATEAU, (32, 33,1)),
            Chemin(NOIR__, 2, 104, TYPE_WAGON_, (32, 34,0)),
            Chemin(BLANC_, 2, 105, TYPE_WAGON_, (32, 34,1)),
            Chemin(ROUGE_, 3, 106, TYPE_BATEAU, (35, 33,0)),
            Chemin(NOIR__, 3, 107, TYPE_BATEAU, (35, 33,1)),
            Chemin(BLANC_, 5, 108, TYPE_WAGON_, (30, 33, 0)),
            Chemin(GRIS__, 2, 109, TYPE_BATEAU, (26,25)),
        ]


    def veut_poser(self, id_joueur):
        """
        demande au joueur quel chemins il veut posser et le pose
        """
        chemin_is_poser = False
        Comu.emition(id_joueur, 'quel chemin veux tu poser ? ')
        reception = Comu.reception()
        while reception != END_COMUNICATION and not chemin_is_poser:
            if int(reception):
                pass


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

    def reliee(self, villeA, villeB, id_joueur, villeC):
        """
        calcule si deux villes sont relier par le joueur id_joueur

        :param villeA:
        :param villeB:
        :param id_joueur:
        :return:
        """
        relier_a_B = self.ville_relier(id_joueur, villeB)

        if villeC is None:
            return villeA in relier_a_B
        return  villeA in relier_a_B and villeC in relier_a_B