from joueur import *


def poser(joueur,chemin):
    """
    verifie si le joueur à les cartes et les wagons necessaire pour pouvoir poser
    """
    couleur = chemin.couleur
    taille = chemin.taille

    if joueur.carte_wagon[couleur] < taille or joueur.nb_wagon < taille   :
        return "impossible pas assez de carte de couleur "
    else :
        joueur.carte_wagon[couleur] -= taille
        joueur.nb_wagon -= taille



