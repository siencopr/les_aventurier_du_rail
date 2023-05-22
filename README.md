# les_aventurier_du_rail

baser sur le jeu, les avanturier du rail, se projet va contenir deux parties majeur : 
 - la parie client :
     - interface graphique
     - comunication avec le serv
 - la partie serveur : 
     - calcule de l'état du jeu
        - representation du plateau (matrice) 
        - pour le joueurs, créé une class (inventaire wagon dico , score , cartes destination list ) **en cours**
        - sur les chemins : calculer si le joueurs a les bonnes cartes + poser des wagons (chemin) - taille du chemin dans les wagons du jouer si pas assez renfovie erreur 
        - carte destination (ville , points)
        - calculer si deux destination sont relier (existe chemin)  ajoute score joueur
        - demander le nombre et le nom des joueurs (lois)
        - pioche (file) piocher et remplacer
        - defausse (liste, si pioche vide : shufle defausse puis add sur la pioche)
        - European express point parcours en profondeur chemin est marqué (mey) 
        - bouton bloqué gerer fin du jeu avec 1 wagon (si pas bloqué -5 point)
        - max 5min pour jouer le tour, au bout de 5 min, next
       <- si next 2 fois de suite, -1 min sur le timer>
       <- bouton quitter> 
     - communication avec le(s) client(s)

 