from joueur import *

matrice = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0]]


def existe_chemin(villeA, villeB, joueur, matrice):
    """
    verifie s'il existe un chemin entre la villeA et la villeB appartenant au joueur JOUEUR
    """

    numA = villeA[1]
    numB = villeB[1]

    print(numA, numB)
    ville_relie_A = []
    for ligne in range(len(matrice)):
        if matrice[ligne][numA] == joueur:
            ville_relie_A += [ligne]

    print(ville_relie_A)
    ville_relie_B = []
    for ligne in range (len(matrice) ):
        if matrice[ligne][numB] == joueur  :
            ville_relie_B += [ligne]
    print(ville_relie_B)
    for k in ville_relie_A :
        if k in ville_relie_B :
            return True
    return False


print(existe_chemin(("a",1),("b",3),1,matrice))