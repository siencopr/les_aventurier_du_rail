from constantes import *

class Destination:
    def __init__(self, villeA, villeB ,points , villeC = None):
        self.ville1 = villeA
        self.ville2 = villeB
        self.ville3 = villeC
        self.points = points
    def __repr__(self):
        if self.ville3 == None :
            return str(self.ville1) + "  <=>  " + str(self.ville2) + "  :  " + str(self.points)
        else :
            return str(self.ville1) + "  <=>  " + str(self.ville2) + "  <=>  " + str(self.ville3) +  "  :  " + str(self.points)

longue_dest = [
Destination(Ville.CedarRapids, Ville.Rouyn, 20),
Destination(Ville.ThunderBay, Ville.Buffalo, 20),
Destination(Ville.Marathon, Ville.NewYork, 22),
Destination(Ville.EauClaire, Ville.Detroit, 20),
Destination(Ville.Montreal, Ville.TraverseCity, 19),
Destination(Ville.Wausau, Ville.Rouyn, 20),
Destination(Ville.Scranton, Ville.Wausau, 20),
Destination(Ville.Marathon, Ville.NewYork, 20),
Destination(Ville.Albany, Ville.Duluth, 20),
Destination(Ville.Montreal, Ville.EauClaire, 23),
Destination(Ville.SaultSteMarie, Ville.NewYork, 20),
Destination(Ville.Chicago, Ville.Ottawa, 19),
Destination(Ville.Marquette, Ville.Scranton, 19),
Destination(Ville.Toronto, Ville.Duluth, 20),
Destination(Ville.SouthBayMouth, Ville.Duluth, 20),
Destination(Ville.Chicago, Ville.Rouyn, 20),
Destination(Ville.Toledo, Ville.ThunderBay, 20),
Destination(Ville.Syracuse, Ville.Marquette, 19),
Destination(Ville.CedarRapids, Ville.Sudbury, 19),
Destination(Ville.BayCity, Ville.Timmins, 19),
Destination(Ville.Scranton, Ville.Rouyn, 21, Ville.SaultSteMarie),
Destination(Ville.Marquette, Ville.Timmins, 21, Ville.Ottawa),
Destination(Ville.Muskegon, Ville.Marquette, 21, Ville.Timmins),
Destination(Ville.PortElgin, Ville.Duluth, 21, Ville.Madison),
Destination(Ville.GreenBay, Ville.BayCity, 19, Ville.Rouyn),
Destination(Ville.Chicago, Ville.Toledo, 20, Ville.PerrySound),
Destination(Ville.Albany, Ville.SouthBend, 21, Ville.EauClaire),
Destination(Ville.Milwaukee, Ville.SouthBayMouth, 19, Ville.Buffalo),
Destination(Ville.Cleveland, Ville.Kingston, 20, Ville.CedarRapids),
Destination(Ville.TraverseCity, Ville.CedarRapids, 21, Ville.ThunderBay),
Destination(Ville.Syracuse, Ville.CedarRapids, 20, Ville.Duluth),
Destination(Ville.SouthBayMouth, Ville.Erie, 19, Ville.Chicago),
Destination(Ville.Toronto, Ville.SouthBend, 21, Ville.Wausau),
Destination(Ville.Toronto, Ville.Montreal, 20, Ville.Timmins),
Destination(Ville.Milwaukee, Ville.PortElgin, 20, Ville.ThunderBay),
]


courte_dest = [
Destination(Ville.CedarRapids, Ville.Duluth, 8),
Destination(Ville.Duluth, Ville.SaultSteMarie, 8),
Destination(Ville.SaultSteMarie, Ville.Madison, 10),
Destination(Ville.Madison, Ville.Cleveland, 9),
Destination(Ville.Cleveland, Ville.SaultSteMarie, 9),
Destination(Ville.SaultSteMarie, Ville.Rouyn, 11),
Destination(Ville.Rouyn, Ville.Toronto, 10),
Destination(Ville.Toronto, Ville.NewYork, 8),
Destination(Ville.NewYork, Ville.Montreal, 9),
Destination(Ville.Montreal, Ville.SouthBayMouth, 9),
Destination(Ville.SouthBayMouth, Ville.Milwaukee, 10),
Destination(Ville.Milwaukee, Ville.Duluth, 11),
Destination(Ville.Duluth, Ville.Timmins, 11),
Destination(Ville.Timmins, Ville.Detroit, 12),
Destination(Ville.Detroit, Ville.NewYork, 14),
Destination(Ville.NewYork, Ville.PerrySound, 12),
Destination(Ville.PerrySound, Ville.TraverseCity, 10),
Destination(Ville.TraverseCity, Ville.EauClaire, 8),
Destination(Ville.EauClaire, Ville.Timmins, 12),
Destination(Ville.Timmins, Ville.GreenBay, 13),



]

for dest in longue_dest :
    print(dest)