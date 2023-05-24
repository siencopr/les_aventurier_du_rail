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
        self.carte_wagon = {CARTE_WAGON_LOCOMOTIVE : 0, CARTE_WAGON_VIOLET : 0, CARTE_WAGON_JAUNE : 0, CARTE_WAGON_ROUGE : 0, CARTE_WAGON_NOIR : 0,
                            CARTE_WAGON_BLANC : 0, CARTE_WAGON_VERT : 0}
        self.ajouter_carte_wagon(carte_wagon)

    def choisir_cartes_destination(self, choix):
        comu.emition(self.id, str('vous devez en choisir au moins une carte destination parmis : ' + str(choix)))
        list_garder = []
        reception = comu.reception()
        while reception != END_COMUNICATION or len(list_garder) == 0:
            if reception in choix and not reception in list_garder:
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