from constantes import *
from comunication import Communication
from plateau import Plateau
from joueur import Joueur
from pioche_defausse import Pioche_Defausse

Communication = Communication()
Destination_calcule = Destination_calcule()
Pioche = Pioche_Defausse()
class Jeu:

    def __init__(self):
        self.nombre_joueurs = None
        self.plateau = Plateau()

        self.l_joueurs = 4*[None]


    def initialisation_partie(self):
        if self.nombre_joueurs is None:
            Communication.emition('all', 'nombre de joueurs ?')
            self.nombre_joueurs = int(Communication.reception())
            assert self.nombre_joueurs <= 4, 'tu veux pas respecter les règles??????'

        for i in range(self.nombre_joueurs):
            self.l_joueurs[i] = Joueur(i, Destination_calcule.piocher_id_destination_depart(), Pioche.distribuer())


    def boucle(self):
        #determiner a qui c le tour
        joueur_en_cour_id = 0
        Pioche.piocher(joueur_en_cour_id)


    def end_game(self):
        ###calcule des points pour les cartes destinations################################################
        for joueur in self.l_joueurs:
            for destination in joueur.carte_destination:
                if self.plateau.reliee(destination.ville1, destination.ville2, joueur.id, destination.ville3):
                    joueur.point += destination.points
                else:
                    joueur.point -= destination.points


