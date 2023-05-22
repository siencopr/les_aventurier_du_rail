from constantes import *

class Destination:
    def __init__(self, villeA, villeB ,points , villeC = None):
        self.ville1 = villeA
        self.ville2 = villeB
        self.ville3 = villeC
        self.points = points
    def __repr__(self):
        if self.ville3 == None :
            return str(self.ville1) + "  <=>  " + str(self.ville2) + "  :  " +str(self.points)
        else :
            return str(self.ville1) + "  <=>  " + str(self.ville2) + "  <=>  " + str(self.ville3) +  "  :  " + str(self.points)

longue_dest = [
Destination(ville.CedarRapids,ville.Rouyn, 20),
Destination(ville.ThunderBay,ville.Buffalo,20),
Destination(ville.Marathon,ville.NewYork,22),
Destination(ville.EauClaire,ville.Detroit,20),
Destination(ville.Montreal,ville.TraverseCity,19),
Destination(ville.Wausau,ville.Rouyn, 20),
Destination(ville.Scranton,ville.Wausau,20),
Destination(ville.Marathon,ville.NewYork,20),
Destination(ville.Albany,ville.Duluth,20),
Destination(ville.Montreal,ville.EauClaire,23),
Destination(ville.SaultSteMarie,ville.NewYork, 20),
Destination(ville.Chicago,ville.Ottawa,19),
Destination(ville.Marquette,ville.Scranton,19),
Destination(ville.Toronto,ville.Duluth,20),
Destination(ville.SouthBayMouth,ville.Duluth,20),
Destination(ville.Chicago,ville.Rouyn, 20),
Destination(ville.Toledo,ville.ThunderBay,20),
Destination(ville.Syracuse,ville.Marquette,19),
Destination(ville.CedarRapids,ville.Sudbury,19),
Destination(ville.BayCity,ville.Timmins,19),
Destination(ville.Scranton,ville.Rouyn,21,ville.SaultSteMarie),
Destination(ville.Marquette,ville.Timmins,21,ville.Ottawa),
Destination(ville.Muskegon,ville.Marquette,21,ville.Timmins),
Destination(ville.PortElgin,ville.Duluth,21,ville.Madison),
Destination(ville.GreenBay,ville.BayCity,19,ville.Rouyn),
Destination(ville.Chicago,ville.Toledo,20,ville.PerrySound),
Destination(ville.Albany,ville.SouthBend,21,ville.EauClaire),
Destination(ville.Milwaukee,ville.SouthBayMouth,19,ville.Buffalo),
Destination(ville.Cleveland,ville.Kingston,20,ville.CedarRapids),
Destination(ville.TraverseCity,ville.CedarRapids,21,ville.ThunderBay),
Destination(ville.Syracuse,ville.CedarRapids,20,ville.Duluth),
Destination(ville.SouthBayMouth,ville.Erie,19,ville.Chicago),
Destination(ville.Toronto,ville.SouthBend,21,ville.Wausau),
Destination(ville.Toronto,ville.Montreal,20,ville.Timmins),
Destination(ville.Milwaukee,ville.PortElgin,20,ville.ThunderBay),
]
for dest in longue_dest :
    print(dest)