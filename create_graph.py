import random as rd

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

class Graphe_list:
    
    def __init__(self):
        dt1 = Data_Tier1()
        dt2 = Data_Tier2()
        self.resaux = self.create_tier1(dt1)
        self.resaux += self.create_tier2(dt2, dt1.n)
        self.resaux += self.create_tier3(dt1.n, dt2.n)
        print(len(self.resaux))
    
    
    def create_tier1(self, dt):
        tier = []
        for i in range(dt.n):
            temps = []
            parents = []
            for j in range(dt.n):
                if rd.random() <= dt.pourcentage:
                    temps.append(rd.randint(dt.temps[0], dt.temps[1]))
                    parents.append(rd.randint(0, dt.n))
            tier.append(Sommet(temps, parents))
        return tier

    def create_tier2(self, dt, tier1_n):
        tier = []
        for i in range(dt.n):
            parents = []
            temps = []
            for j in range(rd.randint(dt.liens_t1[0], dt.liens_t1[1])):
                parents.append(rd.randint(0, tier1_n))
                temps.append(rd.randint(dt.temps[0], dt.temps[1]))
            for j in range(rd.randint(dt.liens_t2[0], dt.liens_t2[1])):
                parents.append(rd.randint(tier1_n, dt.n + tier1_n))
                temps.append(rd.randint(dt.temps[0], dt.temps[1]))
            tier.append(Sommet(temps, parents))
        return tier

    def create_tier3(self, tier1_n, tier2_n):
        dt = Data_Tier3()
        tier = []
        for i in range(dt.n):
            parents = []
            temps = []
            for j in range(dt.liens_t2):
                parents.append(rd.randint(tier1_n, tier1_n+tier2_n))
                temps.append(rd.randint(dt.temps[0], dt.temps[1]))
            tier.append(Sommet(temps, parents))
        return tier
        

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

