import random as rd
from math import ceil
from data import *
import numpy as np

np.random.seed(3)

"""Create graph"""

class Sommet:
    def __init__(self, temps, parents):
        self.temps = temps
        self.parents = parents #faire enfant? non - car la table de routage est figee
    
    def append_edge(self, temps, parent):
        self.temps.append(temps)
        self.parents.append(parent)



class Graphe_list:
    
    def __init__(self, add_2parents = False):
        self.add_2parents = add_2parents

        self.reseaux = self.create_tier1()
        connexe = self.is_connexe()
        while not connexe:
            self.reseaux = self.create_tier1()
            connexe = self.is_connexe()
        self.reseaux = self.create_tier2(self.reseaux)
        self.reseaux = self.create_tier3(self.reseaux)
    
    
    def create_tier1(self):

        tier = [Sommet([], []) for i in range(data_tier1.n)]
        for i in range(data_tier1.n):
            for j in range(i+1, data_tier1.n):
                if rd.random() <= data_tier1.pourcentage:
                    temps = rd.randint(data_tier1.temps[0], data_tier1.temps[1])
                    self.update_tier(tier, i, j, temps)
        return tier

    def create_tier2(self, tier):
        tier_len = len(tier)
        new_tier = [Sommet([], []) for i in range(data_tier2.n)]
        tier += new_tier

        for i in range(data_tier2.n):
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
                self.choose_parent(data_tier1.n, data_tier2.n+data_tier1.n-1, i+tier_len, data_tier3, tier)
        return tier
    
    def choose_parent(self, d, f, i, data_tier, tier):
        parent = (rd.randint(d, f)) 
        temps = (rd.randint(data_tier.temps[0], data_tier.temps[1]))
        while (parent in tier[i].parents) or (parent == i):
            parent = (rd.randint(d, f))
        self.update_tier(tier, i, parent, temps)

    def update_tier(self, tier, i, parent, temps):
        tier[i].append_edge(temps, parent)
        if self.add_2parents:
            tier[parent].append_edge(temps, i) #doublons !!!
    
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



def matrice_graphe(reseau_graphe):
    taille = len(reseau_graphe)
    matrice_graphe = [[float('inf')] * taille for _ in range(taille)] #inf = infini, au lieu de 0 ou -1

    for i in range(taille): 
        parents = reseau_graphe[i].parents
        temps = reseau_graphe[i].temps
        if parents: 
            for j in range(len(parents)): #on parcourt les parents de chaque sommet
                matrice_graphe[parents[j]][i] = temps[j] #[ligne][colonne] = [parent][fils]
    return matrice_graphe


def algo_de_Floyd_Warshall(matrice):
    taille = len(matrice)
    P = [[-1] * taille for _ in range(taille)] #matrice des prédecesseurs
    for k in range (taille): #k représente un sommet intérmediaire
        for i in range (taille):
            for j in range (taille):
                if (matrice[i][k] + matrice[k][j]) < matrice[i][j]:
                    matrice[i][j] = matrice[i][k] + matrice[k][j]
                    if i != j:
                        P[i][j] = k
    return matrice, P  #P[i][j] c'est le predecesseur de j dans le plus court chemin de i à j 


def chemin_le_plus_court(i, j, tab_pred): 
    chemin = [] 
    predecesseur = tab_pred[i][j]
    while predecesseur != -1 and predecesseur != i: #-1 veut dire qu'il n'y a pas de pred dans le chemin le plus court établi
        chemin.append(predecesseur)
        predecesseur = tab_pred[i][predecesseur]
    chemin.reverse()
    chemin.insert(0, i)
    chemin.append(j)

    #print('Le chemin le plus court de', i, 'à', j, 'est', chemin)
    return chemin

def temps_le_plus_court(reseau, chemin):
    temps_tot = 0
    vu = []
    for i in reversed(range(1, len(chemin))):
        try:
            j = reseau[chemin[i]].parents.index(chemin[i-1])
            temps_tot += reseau[chemin[i]].temps[j]
            vu.append(i-1)
        except ValueError: pass
    for i in range(len(chemin)-1):
        if i not in vu:
            try:
                j = reseau[chemin[i]].parents.index(chemin[i+1])
                temps_tot += reseau[chemin[i]].temps[j]
                vu.append(i-1)
            except ValueError: pass
    return temps_tot
    
if __name__ == '__main__':
    graph = Graphe_list()
    reseau = graph.reseaux
    #print(reseau)

    ''' CREATION TABLE DE ROUTAGE '''
    _, tab_predecesseurs = algo_de_Floyd_Warshall(matrice_graphe(reseau))
    #print(tab_predecesseurs)
    debut = 0 #varient
    arrivée = 99
    chemin_le_plus_court(debut, arrivée, tab_predecesseurs)
    

    if graph.is_connexe() == True :
        print(graph.is_connexe(), 'le graphe est connexe')
    else : 
        print(graph.is_connexe(), "le graphe n'est pas connexe")

    '''
    c = 0
    for i in reseau:
        print(c, i.parents)
        print(c, i.temps)
        c += 1
       ''' 
    
