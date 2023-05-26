# les_aventurier_du_rail

baser sur le jeu, les avanturier du rail, se projet va contenir deux parties majeur : 
 - la partie client :
     - interface graphique
     - Cartes destinations longues et courte ***ok***
     - Cartes wagons ***ok***
     - Plateau ***ok***
     - Pions et wagons
     - comunication avec le serv
 - la partie serveur : 
     - calcule de l'état du jeu
        - representation du plateau (matrice) ***ok***
        - associe une ville à un numéro ***ok***
        - classe carte destination ***ok***
        - pour le joueurs, créé une class (inventaire wagon dico , score , cartes destination list ) ***ok***
        - poser des wagons (chemin) ***ok***
        - calculer si deux destination sont relier (existe chemin)  ***ok***
        - 
        - ***TO SEE :*** ajoute score joueur ( pour les destinations accomplis dans la methode relié de la classe plateau il faut ajouter au joueur le nombre de point de la destination , pour appeller le joueur par son id il faut une dico { id_joueur : objet joueur }
        - 
        - demander le nombre et le nom des joueurs (lois)***en cours***
        - pioche (file) piocher et remplacer***en cour***
        - defausse (liste, si pioche vide : shufle defausse puis add sur la pioche)***ok***
        - European express point parcours en profondeur chemin est marqué (mey) ***ok***
        - bouton bloqué gerer fin du jeu avec 1 wagon (si pas bloqué -5 point)
        - max 5min pour jouer le tour, au bout de 5 min, next
       <- si next 2 fois de suite, -1 min sur le timer>
       <- bouton quitter> 
     - communication avec le(s) client(s)

STATISTIQUES :
37 villes en tout 
110 chemins
