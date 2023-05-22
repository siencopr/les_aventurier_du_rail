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


courte_dest = [
Destination(ville.CedarRapids,ville.Duluth, 8),
Destination(ville.Duluth,ville.SaultSteMarie,8),
Destination(ville.SaultSteMarie,ville.Madison,10),
Destination(ville.Madison,ville.Cleveland,9),
Destination(ville.Cleveland,ville.SaultSteMarie,9),
Destination(ville.SaultSteMarie,ville.Rouyn, 11),
Destination(ville.Rouyn,ville.Toronto,10),
Destination(ville.Toronto,ville.NewYork,8),
Destination(ville.NewYork,ville.Montreal,9),
Destination(ville.Montreal,ville.SouthBayMouth,9),
Destination(ville.SouthBayMouth,ville.Milwaukee, 10),
Destination(ville.Milwaukee,ville.Duluth,11),
Destination(ville.Duluth,ville.Timmins,11),
Destination(ville.Timmins,ville.Detroit,12),
Destination(ville.Detroit,ville.NewYork,14),
Destination(ville.NewYork,ville.PerrySound, 12),
Destination(ville.PerrySound,ville.TraverseCity,10),
Destination(ville.TraverseCity,ville.EauClaire,8),
Destination(ville.EauClaire,ville.Timmins,12),
Destination(ville.Timmins,ville.GreenBay,13),



]

for dest in longue_dest :
    print(dest)