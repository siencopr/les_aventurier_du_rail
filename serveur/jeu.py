from constantes import *
import random
class Jeu:

    def __init__(self):
        self.pioch_init = 18*[CARTE_WAGON_JAUNE, CARTE_WAGON_BLANC, CARTE_WAGON_NOIR, CARTE_WAGON_ROUGE, CARTE_WAGON_LOCOMOTIVE, CARTE_WAGON_VERT, CARTE_WAGON_VIOLET]
        self.pioch_init = random.shuffle(self.pioch_init)

        self.pioche = 'file'
        self.defausse = []

        #je sais pas ou le mettre :
        if self.pioche < 2 :
             self.pioche = random.shuffle(self.defausse)

        self.j1 = None
        self.j2 = None