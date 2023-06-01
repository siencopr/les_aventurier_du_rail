from constantes import *
from comunication import Communication
from plateau import Plateau
from joueur import Joueur

Communication = Communication()
Destination_calcule = Destination_calcule()
class Jeu:

    def __init__(self):
        self.nombre_joueurs = None
        self.plateau = Plateau()

        self.l_joueurs = []
        self.j1 = None
        self.j2 = None


    def initialisation_partie(self):
        if self.nombre_joueurs is None:
            Communication.emition('all', 'nombre de joueurs ?')
            self.nombre_joueurs = int(Communication.reception())

        if self.nombre_joueurs == 2:
            self.l_joueurs = [self.j1, self.j2]
            self.j1 = Joueur(1, Destination_calcule.piocher_id_destination_depart(), [JAUNE_, BLANC_, NOIR__, ROUGE_])
    def boucle(self):
        pass

    def end_game(self):
        ###calcule des points pour les cartes destinations################################################
        for joueur in self.l_joueurs:
            for destination in joueur.carte_destination:
                if self.plateau.reliee(destination.ville1, destination.ville2, joueur.id, destination.ville3):
                    joueur.point += destination.points
                else:
                    joueur.point -= destination.points


