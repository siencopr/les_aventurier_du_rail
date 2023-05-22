from constantes import *
class Chemin:
    def __init__(self, couleur, taille, numero, type, villeA, villeB):
        self.couleur = couleur
        self.taille = taille
        self.numero = numero
        self.type = type
        self.joueur_detenteur = None
        self.point = DICO_EQUIVALANCE_LONGUEUR_POINTS[self.taille]
        self.relie = (villeA, villeB)
    def __repr__(self):
        return self.numero

