import math
from data import *

def tiers_cercle(rayon, center, nb_points):
    """Calcule les coordonnes des points
    appartenant a un cercles et equidistints entre eux"""
    coords = []
    i = 0
    while i < math.pi*2:
        x = center[0] + rayon * math.sin(i)
        y = center[1] + rayon * math.cos(i)
        coords.append((x,y))
        i += math.pi * 2 / nb_points

    return coords
    

def tiers_representations(root, width, height, center = None, factor = 1):
    """Retourne les coodonnes des noeuds du reseau"""
    tiers_w = int(width*0.95)
    tiers_h = int(height*0.95)

    rayon = int(min(tiers_w, tiers_h)/2)
    
    if center == None:
        center = [int(tiers_w/2), int(tiers_h/2)+15]
        
    cercles = [] #tier1, tier2, tier3
    nb_tiers = [data_tier1.n, data_tier2.n, data_tier3.n]
    for i in range(3):
        cercles += tiers_cercle(int(rayon/3)*(i+1), center, nb_tiers[i])
    return cercles


