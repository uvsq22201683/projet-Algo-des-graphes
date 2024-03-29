import random as rd
from math import ceil


""" Data classes"""

class Data_Tier1:
    n = 10
    pourcentage = 0.75
    temps = (5, 10)

class Data_Tier2:
    n = 20
    liens_t1 = (1, 2)
    liens_t2 = (2, 3)
    temps = (10, 20)

class Data_Tier3:
    n = 70
    liens_t2 = 2
    temps = (20, 50)



"""Create graph"""

class Sommet:
    def __init__(self, temps = [], parents = []):
        self.temps = temps
        self.parents = parents #faire enfant? non - car la table de routage est figee
    
    def append(self, temps, parent):
        self.temps.append(temps)
        self.parents.append(parent)



class Graphe_list:
    
    def __init__(self):
        dt1 = Data_Tier1()
        self.reseaux = self.create_tier1(dt1)
        self.reseaux = self.create_tier2(self.reseaux)
        self.reseaux = self.create_tier3(dt1.n, self.reseaux)
        print(len(self.reseaux))
    
    
    def create_tier1(self, dt):

        tier = [Sommet() for i in range(dt.n)]
        for i in range(dt.n):
            for j in range(i, dt.n):
                if rd.random() <= dt.pourcentage:
                    temps = rd.randint(dt.temps[0], dt.temps[1])
                    parent = rd.randint(0, dt.n-1)
                    self.update_tier(tier, i, parent, temps)
        return tier

    def create_tier2(self, tier):
        dt = Data_Tier2()
        tier1_n = len(tier)
        new_tier = [Sommet() for i in range(dt.n)]
        tier += new_tier

        for i in range(dt.n):

            for j in range(rd.randint(dt.liens_t1[0], dt.liens_t1[1])):
                parent = (rd.randint(0, tier1_n))
                temps = (rd.randint(dt.temps[0], dt.temps[1]))
                self.update_tier(tier, i, parent, temps)

            for j in range(i, rd.randint(dt.liens_t2[0], dt.liens_t2[1])):
                parent = rd.randint(tier1_n-1, dt.n + tier1_n-1)
                temps = rd.randint(dt.temps[0], dt.temps[1])
                self.update_tier(tier, i, parent, temps)
        return tier

    def create_tier3(self, tier1_n, tier):
        dt = Data_Tier3()
        tier2_n = len(tier) - tier1_n
        new_tier = [Sommet() for i in range(dt.n)]
        tier += new_tier

        for i in range(dt.n):
            for j in range(dt.liens_t2):
                parent = rd.randint(tier1_n-1, tier1_n+tier2_n-1)
                temps = rd.randint(dt.temps[0], dt.temps[1])
                self.update_tier(tier, i, parent, temps)
        return tier
    
    def update_tier(self, tier, i, parent, temps):
        tier[i].append(temps, parent)
        tier[parent].append(temps, i)

def dfs(tier, start):
    visited = [False] *len(tier)
    stack = [start]
    while stack :
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            for i, neighbor in zip(tier[vertex].temps, tier[vertex].parents)
            if not visited[neighbor]:
                stack.append(neighbor)
    return visited

def is_connexe(tier):
    visited = dfs(tier, 0)
    return all(visited)
dt1 = Data_Tier1()
tier1 = self.create_tier1(dt1)
if is_connexe(tier1):
    print("Le tier 1 est connexe.")
else:
    print("Le tier 1 n'est pas connexe.")
    
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
    
'''

Graphe_list()