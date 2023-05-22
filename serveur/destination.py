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
Destination(ville.GreenBay,ville.Rouyn, 15),
Destination(ville.Rouyn,ville.Kingston,9),
Destination(ville.Kingston,ville.SouthBend,11),
Destination(ville.SouthBend,ville.Wausau,8),
Destination(ville.Wausau,ville.PortElgin,10),
Destination(ville.PortElgin,ville.Rouyn, 11),
Destination(ville.Rouyn,ville.ThunderBay,11),
Destination(ville.ThunderBay,ville.GreenBay,11),
Destination(ville.GreenBay,ville.Buffalo,15),
Destination(ville.Buffalo,ville.Montreal,9),
Destination(ville.Montreal,ville.PortElgin, 10),
Destination(ville.PortElgin,ville.Marquette,10),
Destination(ville.Marquette,ville.Madison,9),
Destination(ville.Madison,ville.Duluth,8),
Destination(ville.Duluth,ville.CedarRapids,10),
Destination(ville.CedarRapids,ville.TraverseCity, 11),
Destination(ville.TraverseCity,ville.Sudbury,10),
Destination(ville.Sudbury,ville.Toledo,10),
Destination(ville.Toledo,ville.SaultSteMarie,11),
Destination(ville.SaultSteMarie,ville.Milwaukee,10),
Destination(ville.Milwaukee,ville.Cleveland,8),
Destination(ville.Cleveland,ville.CedarRapids,12),
Destination(ville.CedarRapids,ville.Toronto,15),
Destination(ville.Toronto,ville.SouthBayMouth, 5),
Destination(ville.SouthBayMouth,ville.Montreal,13),
Destination(ville.Montreal,ville.Detroit,13),
Destination(ville.Detroit,ville.PerrySound,8),
Destination(ville.PerrySound,ville.SouthBend,14),
Destination(ville.SouthBend,ville.EauClaire, 10),
Destination(ville.EauClaire,ville.Muskegon,10),
Destination(ville.Muskegon,ville.SaultSteMarie,7),
Destination(ville.Muskegon,ville.Toronto,9),
Destination(ville.SouthBayMouth,ville.Buffalo,15),
Destination(ville.SouthBayMouth,ville.Wausau, 5),
Destination(ville.ThunderBay,ville.EauClaire,9),
Destination(ville.Toledo,ville.Kingston,11),
Destination(ville.Sudbury,ville.Wausau,14),
Destination(ville.Marquette,ville.Buffalo,14),
Destination(ville.Sudbury,ville.Syracuse,11),
Destination(ville.Buffalo,ville.NewYork,14),
Destination(ville.Syracuse,ville.Rouyn,13),
Destination(ville.Syracuse,ville.BayCity,11),
Destination(ville.Toledo,ville.Kingston,11),
Destination(ville.BayCity,ville.Marquette,13),
Destination(ville.Muskegon,ville.GreenBay,9),
Destination(ville.Syracuse,ville.BayCity,13),
Destination(ville.Chicago,ville.BayCity,10),
Destination(ville.Chicago,ville.Marquette,13),
Destination(ville.Chicago,ville.EauClaire,11),
Destination(ville.ThunderBay,ville.GreenBay,12),
Destination(ville.PortElgin,ville.Chicago,12),
]

dico = {}
for dest in longue_dest :

    if dest.ville1[0] not in dico :
        dico [dest.ville1[0] ] = 1
    else :
        dico[dest.ville1[0]] += 1
    if dest.ville2[0] not in dico :
        dico [dest.ville2[0] ] = 1
    else :
        dico[dest.ville2[0]] += 1
print(dico)