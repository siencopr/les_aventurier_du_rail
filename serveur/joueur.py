from comunication import Communication
comu = Communication()
class Joueur:

    def __init__(self):
        comu.emition('j1', 'nom du joueur')
        self.nom = comu.reception()