from joueur import *

matrice =  4 * [ 4* [0]]
print(matrice)
def existe_chemin(villeA,villeB,joueur,matrice):
    """
    verifie s'il existe un chemin entre la villeA et la villeB appartenant au joueur JOUEUR


    calculer si deux destination sont reliés : je pars du point A et je vois tous les chemins du joueur relité à ce point A si aucun chemin  la carte est raté
    sinon on parcours chaque chemin et ses sous chemins , des qu'on a le point B  qui apparait cest TRUE
    pour  parcourir chaque chemin je prend le numéro de la ville ( matrice i * j ) donc numéro de la ville A c'est le I et
     aller à tous les A* j et explorer chacun
en gros A*j voir dans la colonne A toutes les lignes qui ont comme A x j le joueur comme dententeur du trajet et le j qui
correspond devient un A pour un paracours avec coordonnées
    """
    chemins_marqués = []
    numA = min(villeA[0],villeB[0])
    numB = Ville_ojectif[1]
    for ligne in range len(matrice) :
        if matrice[numA][ligne] == joueur.id  :
            if ligne == numB :
                return True
            #ligne (int) numéro de la ville relié
            if (numA,ligne) not in chemins_marqués :
                chemins_marqués += [(numA,ligne)]
                existe_chemin(ligne, Ville_ojectif, joueur, matrice)

    #Le joeuur ne détient aucun des chemins relié à la ville
    return False


print(existe_chemin())