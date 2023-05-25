from comunication import Communication
from constantes import *
comu = Communication()
class Joueur:

    def __init__(self, id, choix_carte_destination, carte_wagon):
        comu.emition(id, 'nom du joueur')
        self.nom = comu.reception()
        self.point = 0
        self.id = id
        self.nb_wagon = 30
        self.nb_bateaux = 30
        self.carte_destination = self.choisir_cartes_destination(choix_carte_destination)
        self.carte_wagon = {CARTE_WAGON_LOCOMOTIVE: 0,
                            VIOLET: 0,
                            JAUNE_: 0,
                            ROUGE_: 0,
                            NOIR__: 0,
                            BLANC_: 0,
                            VERT__: 0}
        self.ajouter_carte_wagon(carte_wagon)

    def choisir_cartes_destination(self, choix):
        comu.emition(self.id, str('vous devez en choisir au moins une carte destination parmis : ' + str(choix)))
        list_garder = []
        reception = comu.reception()
        while reception != END_COMUNICATION or len(list_garder) == 0:
            if int(reception) in choix and not reception in list_garder:
                list_garder.append(reception)
            else:
                comu.emition(self.id, 'entré non valide')

            reception = comu.reception()

        return list_garder.copy()

    def ajouter_carte_wagon(self, liste_cartes_wagons):
        """
        a partir d'une liste de carte wagon, ajoute les carte correspondante au joueur

        :param liste_cartes_wagons:
        :return:
        """
        for wagon in liste_cartes_wagons:
            self.carte_wagon[wagon] += 1

    def choisir_carte_poser(self, couleur_wagon_demander, taille):
        """
        permet au joueur de choisir les cartes qu'il veut utiliser pour créé le chemin


        """
        carte_donner = []
        if self.carte_wagon[couleur_wagon_demander] + self.carte_wagon[CARTE_WAGON_LOCOMOTIVE] < taille:
            return False
        else:
            while taille != 0:
                comu.emition(self.id, 'choisi une cartes wagons pour créé ton chemin')
                carte_wagon_pose = comu.reception()
                if carte_wagon_pose == ANNULATION_CHOIX_CARTE:
                    self.ajouter_carte_wagon(carte_donner)
                    return False

                elif carte_wagon_pose == couleur_wagon_demander or carte_wagon_pose == CARTE_WAGON_LOCOMOTIVE:
                    self.carte_wagon[carte_wagon_pose] -= 1
                    carte_donner.append(carte_wagon_pose)
                    taille -= 1

                else:
                    comu.emition(self.id, 'choix non valide')


            return True

