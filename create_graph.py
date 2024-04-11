import random as rd
from math import ceil
from data import *


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
        return tier

    def create_tier2(self, tier):
        tier_len = len(tier)
        new_tier = [Sommet([], []) for i in range(data_tier2.n)]
        tier += new_tier

        for i in range(data_tier2.n):

            for _ in range(rd.randint(data_tier2.liens_t1[0], data_tier2.liens_t1[1])):
                self.choose_parent(0, data_tier1.n-1, i, data_tier2, tier, tier_len)

            for _ in range(rd.randint(data_tier2.liens_t2[0], data_tier2.liens_t2[1])):
                self.choose_parent(data_tier1.n, data_tier2.n+data_tier1.n-1, i, data_tier2, tier, tier_len)
        return tier

    def create_tier3(self, tier): #ne marche pas
        tier_len = len(tier)
        new_tier = [Sommet([], []) for i in range(data_tier3.n)]
        tier += new_tier

        for i in range(data_tier3.n):
            for _ in range(data_tier3.liens_t2):
                self.choose_parent(data_tier1.n, data_tier2.n+data_tier1.n-1, i, data_tier2, tier, tier_len)
        return tier
    
    def choose_parent(self, d, f, i, data_tier, tier, tier_len):
        parent = (rd.randint(d, f)) 
        temps = (rd.randint(data_tier.temps[0], data_tier.temps[1]))
        while (parent in tier[i].parents) or (parent == i):
            parent = (rd.randint(d, f))
        self.update_tier(tier, i+tier_len, parent, temps)

    def update_tier(self, tier, i, parent, temps):
        tier[i].append_edge(temps, parent)
        tier[parent].append_edge(temps, i) 
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

class Graphe_matrice:
    def __init__(self, n, pourcentage):
        self.tier = self.create_tier(n, pourcentage)

    def create_tier(self, n, pourcentage):
        
        tier = []
        for i in range(n):
            tier1 = []
            for j in range(n):
                if j != i and rd.random() <= pourcentage: #>= ?
                    tier1.append(rd.randint(5,10))
                else:
                    tier1.append(0)
            tier.append(tier1)
        return tier



if __name__ == '__main__':
    graph = Graphe_list()
    reseau = graph.reseaux
    print(reseau[12].parents)
    print(graph.is_connexe())