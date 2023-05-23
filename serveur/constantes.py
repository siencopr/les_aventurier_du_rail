TYPE_BATEAU = 'chemin bateau'
TYPE_WAGON = 'chemin wagon'
# carte wagon
CARTE_WAGON_JAUNE = 'carte wagon jaune'
CARTE_WAGON_ROUGE = 'carte wagon rouge'
CARTE_WAGON_NOIR = 'carte wagon noir'
CARTE_WAGON_VERT = 'carte wagon verre'
CARTE_WAGON_BLANC = 'carte wagon blanc'
CARTE_WAGON_VIOLET = 'carte wagon violet'
CARTE_WAGON_LOCOMOTIVE = 'carte wagon locomotive'
# dico equivalance longueur <=> point
DICO_EQUIVALANCE_LONGUEUR_POINTS = {1: 1, 2: 2, 3: 4, 4: 7, 5: 10, 6: 15, 7: 18, 8: 21, 9: 25}
# comunicaiton
END_COMUNICATION = 'fin des communication, a plus mon reuf'
# couleur chemins
JAUNE = 'jaune'
ROUGE = 'rouge'
NOIR = 'noir'
VERT = 'vert'
BLANC = 'blanc'
VIOLET = 'violet'
GRIS = 'gris'


# liste des villes
class Ville:
    Point2 = ('Point2', 0)
    ThunderBay = ('Thunder Bay', 1)
    Duluth = ('Duluth', 2)
    Marathon = ('Marathon', 3)
    Marquette = ('Marquette', 4)
    Wausau = ('Wausau', 5)
    EauClaire = ('EauClaire', 6)
    Madison = ('Madison', 7)
    CedarRapids = ('Cedar Rapids', 8)
    Chicago = ('Chicago', 9)
    SouthBend = ('South Bend', 10)
    GreenBay = ('Green Bay', 11)
    Milwaukee = ('Milwaukee', 12)
    SaultSteMarie = ('Sault Ste Marie', 13)
    TraverseCity = ('Traverse City', 14)
    Muskegon = ('Muskegon', 15)
    Timmins = ('Timmins', 16)
    Sudbury = ('Sudbury', 17)
    SouthBayMouth = ('South Bay Mouth', 18)
    BayCity = ('Bay City', 19)
    Detroit = ('Detroit', 20)
    Toledo = ('Toledo', 21)
    Cleveland = ('Cleveland', 22)
    PortElgin = ('Port Elgin', 23)
    Toronto = ('Toronto', 24)
    Erie = ('Erie', 25)
    Buffalo = ('Buffalo', 26)
    PerrySound = ('Perry Sound', 27)
    Rouyn = ('Rouyn-Noranda', 28)
    Ottawa = ('Ottawa', 29)
    Montreal = ('Montreal', 30)
    Kingston = ('Kingston', 31)
    Syracuse = ('Syracuse', 32)
    Albany = ('Albany', 33)
    Scranton = ('Scranton', 34)
    NewYork = ('New York', 35)
    Point1 = ('Point1', 36)


class Matrice:
    """
    par convention:

    None indique un chemin non existant
    0 indique que personne ne possède le chemin
    id d'un joueur indique le joueur qui possède le chemin
    """
    matrice_plateau = [
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None], #0
        [None, None, [None, None], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         [None, None]],#1
        [None, [None, None], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         [None, None]],#2
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#3
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#4
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#5
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#6
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#7
        [None, None, None, None, None, None, None, None, None, [None, None], None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#8
        [None, None, None, None, None, None, None, None, [None, None], None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#9
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#10
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#11
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#12
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#13
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#14
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#15
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#16
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#17
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#18
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#19
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#20
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#21
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#22
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#23
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#24
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#25
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#26
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#27
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#28
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#29
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [None, None], None, None,
         None],#30
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#31
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#32
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, [None, None], None, None, None, None, None,
         None],#33
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#34
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],#35
        [None, [None, None], [None, None], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None]]#36
