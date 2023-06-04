from constantes import *
from comunication import Communication
import random
comu = Communication()
class Pioche_Defausse:
    def __init__(self):
        self.Pioche = 30 * [JAUNE_, BLANC_, NOIR__, ROUGE_, CARTE_WAGON_LOCOMOTIVE, VERT__, VIOLET]
        random.shuffle(self.Pioche)
        self.Pioche_visible, self.Pioche = self.Pioche[:5], self.Pioche[6:]
        self.Defausse = []

    def piocher(self, id_joueur):
        tirage_restant = 2
        carte_choisi = []
        while tirage_restant > 0:
            print('visible : ', self.Pioche_visible)
            comu.emition(id_joueur, 'choisi ton action de piochage, il te reste ' + str(tirage_restant) + ' tirages')
            choix = comu.reception()
            if choix == CARTE_WAGON_LOCOMOTIVE:
                if tirage_restant != 2:
                    comu.emition(id_joueur, "pas assez de points")
                elif CARTE_WAGON_LOCOMOTIVE in self.Pioche_visible:
                    carte_choisi.append(CARTE_WAGON_LOCOMOTIVE)
                    self.Pioche.remove(CARTE_WAGON_LOCOMOTIVE)
                    self.Pioche.append(self.Pioche.pop(0))
                    tirage_restant -= 2
                else:
                    comu.emition(id_joueur, "t'as voulu nous bz ?")

            elif choix == PIOCHE_CARTE_CACHER:
                tirage_restant -= 1
                carte_choisi.append(self.Pioche.pop(0))

            elif choix in self.Pioche_visible:
                tirage_restant -= 1
                carte_choisi.append(choix)
                self.Pioche_visible.remove(choix)
                self.Pioche_visible.append(self.Pioche.pop(0))
            else:
                comu.emition(id_joueur, 'tu casse les couilles a choisir comme de la merde')
        return carte_choisi



    def recicler_pioche(self):
        if len(self.Pioche) < 2:
            self.Defausse = random.shuffle(self.Defausse)
            self.Pioche += self.Defausse

    def distribuer(self):
        """
        distribue les 4 carte wagons du debut de partie
        """
        return [self.Pioche.pop(0) for i in range(4)]



