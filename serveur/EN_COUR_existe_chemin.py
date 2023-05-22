

def existe_chemin(s1,s2): #exo 2  
        marque = pp([],s1)
        return s2 in marque
    
    
def pp(graphe,s_marques,s):
    """
    récursive parcourt le graphe en
    profondeur depuis le sommet s. La fonction ajoute les sommets marqués à la liste s_marques 
    """
    if graphe.adj[s] == []:
        s_marques += [s]
    elif s not in s_marques :
        s_marques += [s] 
        for sommet in graphe.adj[s]:
             pp(graphe,s_marques,sommet)  
    return s_marques
