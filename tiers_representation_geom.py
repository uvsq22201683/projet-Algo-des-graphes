import math
import matplotlib.pyplot as plt
from data import *


def tiers_cercle(rayon, center, nb_points):
    coords = []
    i = 0
    while i < math.pi*2:
        x = center[0] + rayon * math.sin(i)
        y = center[1] + rayon * math.cos(i)
        coords.append((x,y))
        i += math.pi * 2 / nb_points

    return coords
    

def tiers_representations(root):
    root.update_idletasks() 
    width = root.winfo_width()
    height = root.winfo_height()
    print(width, height)

    tiers_w = int(width*0.95)
    tiers_h = int(height*0.75)

    rayon = int(min(tiers_w, tiers_h)/2)
    center = (int(width/2), int(tiers_h/2))

    cercles = [] #tier1, tier2, tier3
    nb_tiers = [data_tier1.n, data_tier2.n, data_tier3.n]
    for i in range(3):
        cercles += tiers_cercle(int(rayon/3)*(i+1), center, nb_tiers[i])
    return cercles

if __name__ == '__main__':
    coords = tiers_cercle(10, (5,5), 10)
    print(coords)
    x = []
    y = []
    for i in coords:
        x.append(i[0])
        y.append(i[1])
    plt.scatter(x, y)
    plt.show()

