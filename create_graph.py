import random as rd
from math import ceil
from data import *
import numpy as np


"""Create graph"""

class Sommet:
    def __init__(self, temps, parents):
        self.temps = temps
        self.parents = parents #faire enfant? non - car la table de routage est figee
    
    def append_edge(self, temps, parent):
        self.temps.append(temps)
        self.parents.append(parent)



class Graphe_list:
    
    def __init__(self):
        self.reseaux = self.create_tier1()
        self.reseaux = self.create_tier2(self.reseaux)
        self.reseaux = self.create_tier3(self.reseaux)
    
    
    def create_tier1(self):

        tier = [Sommet([], []) for i in range(data_tier1.n)]
        for i in range(data_tier1.n):
            for j in range(i+1, data_tier1.n):
                if rd.random() <= data_tier1.pourcentage:
                    temps = rd.randint(data_tier1.temps[0], data_tier1.temps[1])
                    #parent = j
                    self.update_tier(tier, i, j, temps)
                    #print(i, tier[i].parents, j)
        return tier

    def create_tier2(self, tier):
        tier_len = len(tier)
        new_tier = [Sommet([], []) for i in range(data_tier2.n)]
        tier += new_tier

        for i in range(data_tier2.n):
            #print(i)

            for _ in range(rd.randint(data_tier2.liens_t1[0], data_tier2.liens_t1[1])):
                self.choose_parent(0, data_tier1.n-1, i+tier_len, data_tier2, tier)

            for _ in range(rd.randint(data_tier2.liens_t2[0], data_tier2.liens_t2[1])):
                self.choose_parent(data_tier1.n, data_tier2.n+data_tier1.n-1, i+tier_len, data_tier2, tier)
        return tier

    def create_tier3(self, tier): #ne marche pas
        tier_len = len(tier)
        new_tier = [Sommet([], []) for i in range(data_tier3.n)]
        tier += new_tier

        for i in range(data_tier3.n):
            for _ in range(data_tier3.liens_t2):
                self.choose_parent(data_tier1.n, data_tier2.n+data_tier1.n-1, i+tier_len, data_tier2, tier)
        return tier
    
    def choose_parent(self, d, f, i, data_tier, tier):
        parent = (rd.randint(d, f)) 
        temps = (rd.randint(data_tier.temps[0], data_tier.temps[1]))
        while (parent in tier[i].parents) or (parent == i):
            parent = (rd.randint(d, f))
        #print(i, tier[i].parents, parent)
        self.update_tier(tier, i, parent, temps)

    def update_tier(self, tier, i, parent, temps):
        tier[i].append_edge(temps, parent)
        tier[parent].append_edge(temps, i) #doublons !!!
    '''
    def is_connexe(self):
        visited = self.dfs(0)
        return all(visited)

    def dfs(self, start):
        visited = [False] * len(self.reseaux)
        stack = [start]
        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                visited[vertex] = True
                for neighbor in self.reseaux[vertex].parents:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return visited
    '''



def matrice_graphe(reseau_graphe):
    matrice_graphe = np.zeros (((len(reseau_graphe)), (len(reseau_graphe))))
    i = 0
    while i < (len(reseau_graphe)): #on remonte les générations, ligne par ligne, parents
        j = 0
        parents = list(set(reseau_graphe[i].parents)) #parents (sans doublons) du sommet en étude
        '''probleeme avec doublons, decalage des valeurs!!!!'''
        temps = reseau_graphe[i].temps
        print(parents, temps, "-")

        if parents: 
            for j in range (len(parents)): #on parcourt les parents de chaque sommet
                print("hola", parents[j], i)
                matrice_graphe[parents[j]][i] = temps[j] #[ligne][colonne] = [parent][fils]
                j +=1
        i += 1
    print(matrice_graphe)
    return matrice_graphe

def algo_de_Floyd_Warshall(matrice):
    mat = matrice
    S = [[-1] * p for p in range(len(matrice))] #matrice des succeseurs
    for k in range (len(matrice)): #k représente un sommet intérmediaire, l'algo vérifie si le chemin entre i et j peut s'améliorer en passant par k
        #P[k][k] = k #k ou 0??
        for i in range (len(matrice)):
            for j in range (len(matrice)):
                if (mat[i][k] + mat[k][j]) < mat[i][j]:
                    mat[i][j] = mat[i][k] + mat[k][j]
                    S[i][j] = k
    return mat, S  #S[i][j] c'est le successuer de i dans le plus court chemin de i à j 

def chemin_le_plus_court(i, j, tab_succ): 
    chemin = [i] 
    prochain = tab_succ[i][j]
    while prochain != -1: #-1 veut dire qu'il n'y a pas de succ dans le chemin le plus court établi
        chemin.append(prochain)
        prochain = tab_succ[prochain][j]
    chemin.append(j)
    print('Le chemin le plus court depuis', i, "jusqu'à", j, 'est', chemin)
    return chemin


if __name__ == '__main__':
    graph = Graphe_list()
    reseau = graph.reseaux
    #print(reseau)

    ''' NE PAS EFFACER STP
    _, tab_successeurs = algo_de_Floyd_Warshall(matrice_graphe(reseau))
    debut = 1 #varient
    arrivée = 6
    chemin_le_plus_court(debut, arrivée,tab_successeurs)
    '''

    #print(graph.is_connexe())

    """
    c = 0
    for i in reseau:
        print(c, i.parents)
        print(c, i.temps)
        c += 1
        """