from constantes import *
from joueur import Joueur
from jeu import Jeu

Jeu = Jeu()

Jeu.initialisation_partie()
Jeu.boucle()
print(Jeu.l_joueurs[0])