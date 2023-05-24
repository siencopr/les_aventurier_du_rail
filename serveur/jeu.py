from constantes import *
from comunication import Communication
from joueur import Joueur
import random

Communication = Communication()
Destination_calcule = Destination_calcule()
class Jeu:

    def __init__(self):
        self.pioch_init = 18*[CARTE_WAGON_JAUNE, CARTE_WAGON_BLANC, CARTE_WAGON_NOIR, CARTE_WAGON_ROUGE, CARTE_WAGON_LOCOMOTIVE, CARTE_WAGON_VERT, CARTE_WAGON_VIOLET]
        self.pioch_init = random.shuffle(self.pioch_init)

        self.pioche = 'file'
        self.defausse = []


        self.nombre_joueurs = None


        self.j1 = None
        self.j2 = None


    def initialisation_partie(self):
        if self.nombre_joueurs is None:
            Communication.emition('all', 'nombre de joueurs ?')
            self.nombre_joueurs = int(Communication.reception())

        if self.nombre_joueurs == 2:
            self.j1 = Joueur(1, Destination_calcule.piocher_id_destination_depart(), [CARTE_WAGON_JAUNE, CARTE_WAGON_BLANC, CARTE_WAGON_NOIR, CARTE_WAGON_ROUGE])
    def boucle(self):
        pass


