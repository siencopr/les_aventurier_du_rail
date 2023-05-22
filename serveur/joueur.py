from comunication import Communication
from constantes import *
comu = Communication()
class Joueur:

    def __init__(self, id, choix_carte_destination, carte_wagon):
        comu.emition(id, 'nom du joueur')
        self.nom = comu.reception()
        self.point = 0
        self.id = id
        self.nb_wagon = 45
        self.carte_destination = self.choisir_cartes_destination(choix_carte_destination)
        self.carte_wagon = carte_wagon

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

