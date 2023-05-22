from constantes import *
class Chemin:
    def __int__(self, couleur, taille, numero, type):
        self.couleur = couleur
        self.taille = taille
        self.numero = numero
        self.type = type
        self.joueur_detenteur = None
        self.point = DICO_EQUIVALANCE_LONGUEUR_POINTS[self.taille]
    def __repr__(self):
        return self.numero