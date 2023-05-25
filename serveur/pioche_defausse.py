from constantes import *
from comunication import Communication
import random
comu = Communication()
class Pioche_Defausse:
    def __init__(self):
        self.Pioche = 30 * [JAUNE_, BLANC_, NOIR__, ROUGE_, CARTE_WAGON_LOCOMOTIVE, VERT__, VIOLET]
        self.Pioche = random.shuffle(self.Pioche)
        self.Pioche_visible, self.Pioche = self.Pioche[:5], self.Pioche[6:]
        self.Defausse = []

    def piocher(self, id_joueur):
        tirage_restant = 2
        carte_choisi = []
        comu.emition(id_joueur, 'choisi ton action de piochage, il te reste' + str(tirage_restant) + 'tirages')
        while tirage_restant != 0:
            choix = comu.reception()
            if choix == CARTE_WAGON_LOCOMOTIVE and tirage_restant == 2:
                carte_choisi.append(CARTE_WAGON_LOCOMOTIVE)
                tirage_restant -= 2
            elif choix == PIOCHE_CARTE_CACHER :
                tirage_restant -= 1
                carte_choisi.append(self.Pioche.pop(0))
                "ne peut prend qu'une autre carte de la pioche"
            elif choix in self.Pioche_visible :
                tirage_restant -= 1
                carte_choisi.append(choix)
            else:
                comu.emition(id_joueur, 'tu casse les couilles a choisir comme de la merde')



    def recicler_pioche(self):
        if len(self.Pioche) < 2:
            self.Defausse = random.shuffle(self.Defausse)
            self.Pioche += self.Defausse



