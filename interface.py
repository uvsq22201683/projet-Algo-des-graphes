import tkinter as tk
from tiers_representation_geom import tiers_representations
from data import *
from create_graph import Graphe_list

def tier(root, color, nb,  coords):
    t = tk.Label(root, text = nb, fg = color)
    t.place(x = coords[0], y = coords[1])

def place_tier(root):
    #global root
    tiers_coords = tiers_representations(root)
    color =  data_tier1.color
    for j in range(len(tiers_coords)):
        tier(root, color, j, tiers_coords[j])
        if j == data_tier1.n-1:
            color = data_tier2.color
        elif j == data_tier2.n+data_tier1.n-1:
            color = data_tier3.color
    return tiers_coords

def add_liens(canva, coords):
    reseau = Graphe_list().reseaux
    color =  data_tier3.color

    for i in reversed(range(len(reseau))):
        for j in range(len(reseau[i].parents)):
            canva.create_line(coords[i][0], coords[i][1], 
                              coords[reseau[i].parents[j]][0], coords[reseau[i].parents[j]][1],
                              fill = color)
        if i == data_tier1.n:
            color = data_tier1.color
        elif i == data_tier2.n+data_tier1.n:
            color = data_tier2.color

    


def main():
    root = tk.Tk()
    root.title('Algo des graphes')
    root.config(bg = "#C0BCB5")
    root.geometry("800x600") 
    #root.resizable(width = False, height = False) 

    root.update_idletasks() 
    canva = tk.Canvas(root, width=root.winfo_width(), height = root.winfo_height(), bg="ivory")
    canva.place(x = 0, y = 0)

    coords = place_tier(root)
    add_liens(canva, coords)
    
    #root.bind("<Configure>", place_tier)
    root.mainloop()

main()
