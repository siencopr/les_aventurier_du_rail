from constantes import *
class Chemin:
    def __init__(self, couleur, taille, numero, type, link_matrice):
        assert len(link_matrice) >= 2, "le lien vers la matrice pose problème"
        self.couleur = couleur
        self.taille = taille
        self.numero = numero
        self.joueur_detenteur = None
        self.point = DICO_EQUIVALANCE_LONGUEUR_POINTS[self.taille]
        self.link_matrice_plateau = link_matrice
        self.type = type
        self.modifier_detenteur(0)
    def modifier_detenteur(self, new_valeur): # plutot modifier valeur
        self.type = new_valeur
        if len(self.link_matrice_plateau) == 2:
            Matrice.matrice_plateau[self.link_matrice_plateau[0]][self.link_matrice_plateau[1]] = new_valeur
        else:
            Matrice.matrice_plateau[self.link_matrice_plateau[0]][self.link_matrice_plateau[1]][self.link_matrice_plateau[2]] = new_valeur