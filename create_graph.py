import random as rd
from data import *
from math import inf


global add_2parents 
add_2parents= False #ne pas garder des donnes redondantes

"""Create graph"""

class Sommet:
    def __init__(self, temps, parents):
        self.temps = temps
        self.parents = parents 
    
    def append_edge(self, temps, parent):
        self.temps.append(temps)
        self.parents.append(parent)



class Graphe_list:
    
    def __init__(self, add_2parents = add_2parents):
        """Creer le graphe"""
        self.create_tier1()

        connexe = self.is_connexe()
        while not connexe:
            self.create_tier1()
            connexe = self.is_connexe()
            print(self.reseaux, connexe)

        self.create_tier2()
        self.create_tier3()

        self.matrice_temps, self.tab_pred = self.dijkstra_2D() #

        if not add_2parents:
            self.delete_doublon()
    
    
    def create_tier1(self):
        """Creer noeuds du tier 1"""
        self.reseaux = [Sommet([], []) for i in range(data_tier1.n)]

        for i in range(data_tier1.n):
            for j in range(i+1, data_tier1.n):
                if rd.random() <= data_tier1.pourcentage:
                    temps = rd.randint(data_tier1.temps[0], data_tier1.temps[1])
                    self.update_tier(i, j, temps)

    def create_tier2(self):
        """Creer noeuds du tier 2"""
        tier_len = len(self.reseaux)
        new_tier = [Sommet([], []) for i in range(data_tier2.n)]
        self.reseaux += new_tier

        for i in range(data_tier2.n):
            for _ in range(rd.randint(data_tier2.liens_t1[0], data_tier2.liens_t1[1])):
                self.choose_parent(0, data_tier1.n-1, i+tier_len, data_tier2)

            for _ in range(rd.randint(data_tier2.liens_t2[0], data_tier2.liens_t2[1])):
                self.choose_parent(data_tier1.n, data_tier2.n+data_tier1.n-1, 
                                   i+tier_len, data_tier2)


    def create_tier3(self):
        """Creer noeuds du tier 3"""
        tier_len = len(self.reseaux)
        new_tier = [Sommet([], []) for i in range(data_tier3.n)]
        self.reseaux += new_tier

        for i in range(data_tier3.n):
            for _ in range(data_tier3.liens_t2):
                self.choose_parent(data_tier1.n, data_tier2.n+data_tier1.n-1, 
                                   i+tier_len, data_tier3)
    
    def choose_parent(self, d, f, i, data_tier):
        """Attribuer les temps et les parents aux noeuds"""
        parent = rd.randint(d, f)
        temps = rd.randint(data_tier.temps[0], data_tier.temps[1])
        while (parent in self.reseaux[i].parents) or (parent == i):
            parent = rd.randint(d, f)
        self.update_tier(i, parent, temps)

    def update_tier(self, i, parent, temps):
        """Sauvegarder les temps et les parents attribues aux noeuds"""
        self.reseaux[i].append_edge(temps, parent)
        self.reseaux[parent].append_edge(temps, i)
    
    ###Connexite
    
    def is_connexe(self):
        """Verifie la connexite du graphe"""
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
    
    #Supprimer les donnes doublees
    
    def delete_doublon(self):
        """Supprimer les donnes redondantes du graphe"""
        for i in range(len(self.reseaux)):
            for j in range(len(self.reseaux[i].parents)):
                p = self.reseaux[i].parents[j]
                try:
                    idx = self.reseaux[p].parents.index(i)
                    self.reseaux[p].parents.remove(idx)
                    self.reseaux[p].temps.remove(idx)
                except ValueError: pass
    
    # Table de routage

    def dijkstra_2D(self):
        """Creation d'une table de routage grace a l'algorithme du dijkstra"""
        n = len(self.reseaux)
        matrice = [[0 for _ in range(n)]for __ in range(n)]
        parent = [[0 for _ in range(n)]for __ in range(n)]
        for debut in range(n):
            parent[debut], matrice[debut] = self.dijkstra(debut)
        return matrice, parent
    
    def dijkstra(self, debut):
        """Application de l'algorithme du dijkstra a un noeud donne"""
        n = len(self.reseaux)
        matrice = [inf for _ in range(n)]
        matrice[debut] = 0
        parent = [0 for _ in range(n)]
        vu = []
        d_pre = debut
        while len(vu) != n:
            d_min = (0, inf)
            voisins = self.reseaux[d_pre].parents
            temps = self.reseaux[d_pre].temps
            for i in range(len(voisins)):
                if voisins[i] not in vu:
                    if temps[i] + matrice[d_pre] < matrice[voisins[i]]:
                            matrice[voisins[i]] = temps[i] + matrice[d_pre]
                            parent[voisins[i]] = d_pre
                    if matrice[voisins[i]] < d_min[1]:
                        d_min = (voisins[i], matrice[voisins[i]])
            vu.append(d_pre)
            d_pre = d_min[0]
        return parent, matrice
    
    def chemin_le_plus_court(self, i, j):
        """Trouver le chemin le plus court entre 2 noeuds 
        a base d'une table de routage"""
        path = [j]
        while path[-1] != i:
            path.append(self.tab_pred[i][path[-1]])
        path.reverse()
        return path
    


