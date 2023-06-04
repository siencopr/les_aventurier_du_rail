from comunication import Communication
from constantes import *
comu = Communication()
class Joueur:

    def __init__(self, id, choix_carte_destination, carte_wagon):
        comu.emition(id, 'nom du joueur')
        self.nom = comu.reception()
        self.point = 0
        self.id = id
        self.nb_bateau_wagons = {TYPE_BATEAU : 30, TYPE_WAGON_ : 30}
        self.carte_destination = self.choisir_cartes_destination(choix_carte_destination)
        self.carte_wagon = {CARTE_WAGON_LOCOMOTIVE: 0,
                            VIOLET: 0,
                            JAUNE_: 0,
                            ROUGE_: 0,
                            NOIR__: 0,
                            BLANC_: 0,
                            VERT__: 0}
        self.ajouter_carte_wagon(carte_wagon)

    def __repr__(self):
        print('nom :', self.nom)
        print('id :', self.id)
        print('cartes wagons : ', self.carte_wagon)
        print('carte destinations', self.carte_destination)
        print('point : ', self.point)
        print(self.nb_bateau_wagons)
        return '\n \n'

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

    def choisir_carte_poser(self, couleur, taille, type):
        """
        permet au joueur de choisir les cartes qu'il veut utiliser pour créé le chemin
        """
        couleur_wagon_demander = couleur
        carte_donner = []
        if couleur_wagon_demander == GRIS__:
            comu.emition(self.id, 'quel couleur veut tu choisir ?')
            couleur_wagon_demander = comu.reception()
            if self.carte_wagon[couleur_wagon_demander] >= taille:
                self.carte_wagon[couleur_wagon_demander] -= taille
                return True

        elif self.carte_wagon[couleur_wagon_demander] + self.carte_wagon[CARTE_WAGON_LOCOMOTIVE] < taille or self.nb_bateau_wagons[type] < taille:
            return False

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

