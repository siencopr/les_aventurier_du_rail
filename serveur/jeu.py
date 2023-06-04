from constantes import *
from comunication import Communication
from plateau import Plateau
from joueur import Joueur
from pioche_defausse import Pioche_Defausse

Comu = Communication()
Destination_calcule = Destination_calcule()
Pioche = Pioche_Defausse()
Plateau = Plateau()
class Jeu:

    def __init__(self):
        self.nombre_joueurs = None
        self.l_joueurs = 4*[None]


    def initialisation_partie(self):
        if self.nombre_joueurs is None:
            Comu.emition('all', 'nombre de joueurs ?')
            self.nombre_joueurs = int(Comu.reception())
            assert self.nombre_joueurs <= 4, 'tu veux pas respecter les règles??????'

        for i in range(self.nombre_joueurs):
            self.l_joueurs[i] = Joueur(i, Destination_calcule.piocher_id_destination_depart(), Pioche.distribuer())


    def boucle(self):
        #determiner a qui c le tour
        joueur_en_cour_id = 0
        print(self.l_joueurs[joueur_en_cour_id])
        Comu.emition(joueur_en_cour_id, "que veux tu faire")
        recep = Comu.reception()
        if recep == "piocher":
            self.l_joueurs[joueur_en_cour_id].ajouter_carte_wagon(Pioche.piocher(joueur_en_cour_id))
        elif recep == "poser":
            Plateau.veut_poser(self.l_joueurs[joueur_en_cour_id])
        elif recep == 'carte destination':
            self.l_joueurs[joueur_en_cour_id].carte_destination += self.l_joueurs[joueur_en_cour_id].choisir_cartes_destination(Destination_calcule.repiocher())


    def end_game(self):
        ###calcule des points pour les cartes destinations################################################
        for joueur in self.l_joueurs:
            for destination in joueur.carte_destination:
                if self.plateau.reliee(destination.ville1, destination.ville2, joueur.id, destination.ville3):
                    joueur.point += destination.points
                else:
                    joueur.point -= destination.points


