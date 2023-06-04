- class Chemin:
    - couleur  taille numero joueur_detenteur point link_matrice_plateau type
    - def poser(self, joueur)
   -  def modifier_detenteur(self, new_valeur): # plutot modifier valeur

- class Destination:
    - id ville1 ville2 ville3 points

- class file:
    - contenue 
    - def est_vide(self):
    - def enfiller_liste(self, liste):
    - def deffiler(self):

- class Jeu:
    - nombre_joueurs  l_joueurs
    - def initialisation_partie(self):
    - def boucle(self):
    - def end_game(self):

- class Joueur:
    - nom   point   id  nb_bateau_wagons  carte_destination carte_wagon
    - def choisir_cartes_destination(self, choix):
    - def ajouter_carte_wagon(self, liste_cartes_wagons):
    - def choisir_carte_poser(self, couleur, taille, type):
         
- class Pioche_Defausse:
    - Pioche  Pioche_visible  Defausse
    - def piocher(self, id_joueur):
    - def recicler_pioche(self):
    - def distribuer(self):

- class Plateau:
    - relier    liste_chemin
    - def veut_poser(self, joueur):
    - def ville_relier(self, id_joueur, num_ville, origine = None):
    - def reliee(self, villeA, villeB, id_joueur):
- class Destination_calcule:
    - destinations_longue
    - destinations_courte
    - def piocher_id_destination_depart(self):