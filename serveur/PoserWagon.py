from joueur import *


def poser(joueur,chemin):
    couleur = chemin.couleur
    taille = chemin.taille

    if joueur.carte_wagon[couleur] < taille or joueur.nb_wagon < taille   :
        return "impossible pas assez de carte de couleur "
    else :
        joueur.carte_wagon[couleur] -= taille
        joueur.nb_wagon -= taille



