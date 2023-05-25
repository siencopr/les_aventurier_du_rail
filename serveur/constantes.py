import random

TYPE_BATEAU = 'chemin bateau'
TYPE_WAGON = 'chemin wagon'
# carte wagon
CARTE_WAGON_LOCOMOTIVE = 'carte wagon locomotive'
# dico equivalance longueur <=> point
DICO_EQUIVALANCE_LONGUEUR_POINTS = {1: 1, 2: 2, 3: 4, 4: 7, 5: 10, 6: 15, 7: 18, 8: 21, 9: 25}
# comunication
PIOCHE_CARTE_CACHER = 'je suis un mec malin qui pocher les cartes fasse cacher'
END_COMUNICATION = 'fin des communication, a plus mon reuf'
ANNULATION_CHOIX_CARTE = 'en fait, je suis casse couille, je veux annuler'
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
    Point2_______ = ('Point2', 0)
    ThunderBay___ = ('Thunder Bay', 1)
    Duluth_______ = ('Duluth', 2)
    Marathon_____ = ('Marathon', 3)
    Marquette____ = ('Marquette____', 4)
    Wausau_______ = ('Wausau_______', 5)
    EauClaire____ = ('EauClaire____', 6)
    Madison______ = ('Madison______', 7)
    CedarRapids__ = ('Cedar Rapids', 8)
    Chicago______ = ('Chicago______', 9)
    SouthBend____ = ('South Bend', 10)
    GreenBay_____ = ('Green Bay', 11)
    Milwaukee____ = ('Milwaukee____', 12)
    SaultSteMarie = ('Sault Ste Marie', 13)
    TraverseCity_ = ('Traverse City', 14)
    Muskegon_____ = ('Muskegon', 15)
    Timmins______ = ('Timmins', 16)
    Sudbury______ = ('Sudbury', 17)
    SouthBayMouth = ('South Bay Mouth', 18)
    BayCity______ = ('Bay City', 19)
    Detroit______ = ('Detroit______', 20)
    Toledo_______ = ('Toledo_______', 21)
    Cleveland____ = ('Cleveland____', 22)
    PortElgin____ = ('Port Elgin', 23)
    Toronto______ = ('Toronto______', 24)
    Erie_________ = ('Erie_________', 25)
    Buffalo______ = ('Buffalo______', 26)
    PerrySound___ = ('Perry Sound', 27)
    Rouyn________ = ('Rouyn________-Noranda', 28)
    Ottawa_______ = ('Ottawa_______', 29)
    Montreal_____ = ('Montreal_____', 30)
    Kingston_____ = ('Kingston_____', 31)
    Syracuse_____ = ('Syracuse_____', 32)
    Albany_______ = ('Albany_______', 33)
    Scranton_____ = ('Scranton_____', 34)
    NewYork______ = ('New York', 35)
    Point1_______ = ('Point1_______', 36)

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

class Destination_calcule:

    def __init__(self):
        from destination import Destination
        self.destinations_longue = [
        Destination(Ville.CedarRapids__, Ville.Rouyn________, 0, 20),
        Destination(Ville.ThunderBay___, Ville.Buffalo______, 1, 20),
        Destination(Ville.Marathon_____, Ville.NewYork______, 2, 22),
        Destination(Ville.EauClaire____, Ville.Detroit______, 3, 20),
        Destination(Ville.Montreal_____, Ville.TraverseCity_, 4, 19),
        Destination(Ville.Wausau_______, Ville.Rouyn________, 5, 20),
        Destination(Ville.Scranton_____, Ville.Wausau_______, 6, 20),
        Destination(Ville.Marathon_____, Ville.NewYork______, 7, 20),
        Destination(Ville.Albany_______, Ville.Duluth_______, 8, 20),
        Destination(Ville.Montreal_____, Ville.EauClaire____, 9, 23),
        Destination(Ville.SaultSteMarie, Ville.NewYork______, 10, 20),
        Destination(Ville.Chicago______, Ville.Ottawa_______, 11, 19),
        Destination(Ville.Marquette____, Ville.Scranton_____, 12, 19),
        Destination(Ville.Toronto______, Ville.Duluth_______, 13, 20),
        Destination(Ville.SouthBayMouth, Ville.Duluth_______, 14, 20),
        Destination(Ville.Chicago______, Ville.Rouyn________, 15, 20),
        Destination(Ville.Toledo_______, Ville.ThunderBay___, 16, 20),
        Destination(Ville.Syracuse_____, Ville.Marquette____, 17, 19),
        Destination(Ville.CedarRapids__, Ville.Sudbury______, 18, 19),
        Destination(Ville.BayCity______, Ville.Timmins______, 19, 19),
        Destination(Ville.Scranton_____, Ville.Rouyn________, 21, 20, Ville.SaultSteMarie),
        Destination(Ville.Marquette____, Ville.Timmins______, 21, 21, Ville.Ottawa_______),
        Destination(Ville.Muskegon_____, Ville.Marquette____, 21, 22, Ville.Timmins______),
        Destination(Ville.PortElgin____, Ville.Duluth_______, 21, 23, Ville.Madison______),
        Destination(Ville.GreenBay_____, Ville.BayCity______, 19, 24, Ville.Rouyn________),
        Destination(Ville.Chicago______, Ville.Toledo_______, 20, 25, Ville.PerrySound___),
        Destination(Ville.Albany_______, Ville.SouthBend____, 21, 26, Ville.EauClaire____),
        Destination(Ville.Milwaukee____, Ville.SouthBayMouth, 19, 27, Ville.Buffalo______),
        Destination(Ville.Cleveland____, Ville.Kingston_____, 20, 28, Ville.CedarRapids__),
        Destination(Ville.TraverseCity_, Ville.CedarRapids__, 21, 29, Ville.ThunderBay___),
        Destination(Ville.Syracuse_____, Ville.CedarRapids__, 20, 30, Ville.Duluth_______),
        Destination(Ville.SouthBayMouth, Ville.Erie_________, 19, 31, Ville.Chicago______),
        Destination(Ville.Toronto______, Ville.SouthBend____, 21, 32, Ville.Wausau_______),
        Destination(Ville.Toronto______, Ville.Montreal_____, 20, 33, Ville.Timmins______),
        Destination(Ville.Milwaukee____, Ville.PortElgin____, 20, 34, Ville.ThunderBay___)
            ]
        self.destinations_courte = [Destination(Ville.CedarRapids__, Ville.Duluth_______, 8, 35),
        Destination(Ville.Duluth_______, Ville.SaultSteMarie, 8, 36),
        Destination(Ville.SaultSteMarie, Ville.Madison______, 10, 37),
        Destination(Ville.Madison______, Ville.Cleveland____, 9, 38),
        Destination(Ville.Cleveland____, Ville.SaultSteMarie, 9, 39),
        Destination(Ville.SaultSteMarie, Ville.Rouyn________, 11, 40),
        Destination(Ville.Rouyn________, Ville.Toronto______, 10, 41),
        Destination(Ville.Toronto______, Ville.NewYork______, 8, 42),
        Destination(Ville.NewYork______, Ville.Montreal_____, 9, 43),
        Destination(Ville.Montreal_____, Ville.SouthBayMouth, 9, 44),
        Destination(Ville.SouthBayMouth, Ville.Milwaukee____, 10, 45),
        Destination(Ville.Milwaukee____, Ville.Duluth_______, 11, 46),
        Destination(Ville.Duluth_______, Ville.Timmins______, 11, 47),
        Destination(Ville.Timmins______, Ville.Detroit______, 12, 48),
        Destination(Ville.Detroit______, Ville.NewYork______, 14, 49),
        Destination(Ville.NewYork______, Ville.PerrySound___, 12, 50),
        Destination(Ville.PerrySound___, Ville.TraverseCity_, 10, 51),
        Destination(Ville.TraverseCity_, Ville.EauClaire____, 8, 52),
        Destination(Ville.EauClaire____, Ville.Timmins______, 12, 53),
        Destination(Ville.Timmins______, Ville.GreenBay_____, 13, 54),
        Destination(Ville.GreenBay_____, Ville.Rouyn________, 15, 55),
        Destination(Ville.Rouyn________, Ville.Kingston_____, 9, 56),
        Destination(Ville.Kingston_____, Ville.SouthBend____, 11, 57),
        Destination(Ville.SouthBend____, Ville.Wausau_______, 8, 58),
        Destination(Ville.Wausau_______, Ville.PortElgin____, 10, 59),
        Destination(Ville.PortElgin____, Ville.Rouyn________, 11, 60),
        Destination(Ville.Rouyn________, Ville.ThunderBay___, 11, 61),
        Destination(Ville.ThunderBay___, Ville.GreenBay_____, 11, 62),
        Destination(Ville.GreenBay_____, Ville.Buffalo______, 15, 63),
        Destination(Ville.Buffalo______, Ville.Montreal_____, 9, 64),
        Destination(Ville.Montreal_____, Ville.PortElgin____, 10, 65),
        Destination(Ville.PortElgin____, Ville.Marquette____, 10, 66),
        Destination(Ville.Marquette____, Ville.Madison______, 9, 67),
        Destination(Ville.Madison______, Ville.Duluth_______, 8, 68),
        Destination(Ville.Duluth_______, Ville.CedarRapids__, 10, 69),
        Destination(Ville.CedarRapids__, Ville.TraverseCity_, 11, 70),
        Destination(Ville.TraverseCity_, Ville.Sudbury______, 10, 71),
        Destination(Ville.Sudbury______, Ville.Toledo_______, 10, 72),
        Destination(Ville.Toledo_______, Ville.SaultSteMarie, 11, 73),
        Destination(Ville.SaultSteMarie, Ville.Milwaukee____, 10, 74),
        Destination(Ville.Milwaukee____, Ville.Cleveland____, 8, 75),
        Destination(Ville.Cleveland____, Ville.CedarRapids__, 12, 76),
        Destination(Ville.CedarRapids__, Ville.Toronto______, 15, 77),
        Destination(Ville.Toronto______, Ville.SouthBayMouth, 5, 78),
        Destination(Ville.SouthBayMouth, Ville.Montreal_____, 13, 79),
        Destination(Ville.Montreal_____, Ville.Detroit______, 13, 80),
        Destination(Ville.Detroit______, Ville.PerrySound___, 8, 81),
        Destination(Ville.PerrySound___, Ville.SouthBend____, 14, 82),
        Destination(Ville.SouthBend____, Ville.EauClaire____, 10, 83),
        Destination(Ville.EauClaire____, Ville.Muskegon_____, 10, 84),
        Destination(Ville.Muskegon_____, Ville.SaultSteMarie, 7, 85),
        Destination(Ville.Muskegon_____, Ville.Toronto______, 9, 86),
        Destination(Ville.SouthBayMouth, Ville.Buffalo______, 15, 87),
        Destination(Ville.SouthBayMouth, Ville.Wausau_______, 5, 88),
        Destination(Ville.ThunderBay___, Ville.EauClaire____, 9, 89),
        Destination(Ville.Toledo_______, Ville.Kingston_____, 11, 90),
        Destination(Ville.Sudbury______, Ville.Wausau_______, 14, 91),
        Destination(Ville.Marquette____, Ville.Buffalo______, 14, 92),
        Destination(Ville.Sudbury______, Ville.Syracuse_____, 11, 93),
        Destination(Ville.Buffalo______, Ville.NewYork______, 14, 94),
        Destination(Ville.Syracuse_____, Ville.Rouyn________, 13, 95),
        Destination(Ville.Syracuse_____, Ville.BayCity______, 11, 96),
        Destination(Ville.Toledo_______, Ville.Kingston_____, 11, 97),
        Destination(Ville.BayCity______, Ville.Marquette____, 13, 98),
        Destination(Ville.Muskegon_____, Ville.GreenBay_____, 9, 99),
        Destination(Ville.Syracuse_____, Ville.BayCity______, 13, 100),
        Destination(Ville.Chicago______, Ville.BayCity______, 10, 101),
        Destination(Ville.Chicago______, Ville.Marquette____, 13, 102),
        Destination(Ville.Chicago______, Ville.EauClaire____, 11, 103),
        Destination(Ville.ThunderBay___, Ville.GreenBay_____, 12, 104),
        Destination(Ville.PortElgin____, Ville.Chicago______, 12, 105),
    ]

    def piocher_id_destination_depart(self):
        return [self.destinations_longue.pop(random.randint(0, len(self.destinations_longue)-1)).id] + [self.destinations_courte.pop(random.randint(0, len(self.destinations_courte)-1)).id for k in range(3)]

