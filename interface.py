import tkinter as tk
from tiers_representation_geom import tiers_representations
from data import *
from create_graph import Graphe_list 
from create_graph import algo_de_Floyd_Warshall
from create_graph import chemin_le_plus_court, temps_le_plus_court
from create_graph import matrice_graphe


"""Graph canvas"""

def tier(color, nb, coords):
    circle_size = 9
    x0 = coords[0]-circle_size
    y0 = coords[1]-circle_size
    x1 = coords[0]+circle_size
    y1 = coords[1]+circle_size
    t = canva.create_oval( x0, y0, x1, y1, outline = color, fill = 'white')
    t_label = canva.create_text(coords[0], coords[1], text= nb)
    tiers.append([t, t_label])

def resize_tiers(factor):
    for i in range(len(tiers)):
        tiers[i][1] *= factor
        tiers[i][2] *= factor
        tiers[i][3] *= factor
        tiers[i][4] *= factor
        canva.coords(tiers[i][0], tiers[i][1], tiers[i][2],
                     tiers[i][3], tiers[i][4])

def place_tier():
    global tiers
    tiers = []
    color =  data_tier1.color
    for j in range(len(tiers_coords)):
        tier(color, j, tiers_coords[j])
        if j == data_tier1.n-1:
            color = data_tier2.color
        elif j == data_tier2.n+data_tier1.n-1:
            color = data_tier3.color

def add_liens(canva):
    color =  data_tier1.color
    for i in reversed(range(len(reseau))):
        for j in range(len(reseau[i].parents)):
            if reseau[i].parents[j] < data_tier1.n:
                color =  data_tier1.color
            else: 
                color =  data_tier2.color

            canva.create_line(tiers_coords[i][0], tiers_coords[i][1], 
                              tiers_coords[reseau[i].parents[j]][0], tiers_coords[reseau[i].parents[j]][1],
                              fill = color, width = (data_tier3.temps[1]-reseau[i].temps[j])*0.04)

def do_zoom(event):
    x = canva.canvasx(event.x)
    y = canva.canvasy(event.y)
    factor = 1.001 ** event.delta
    canva.scale(tk.ALL, x, y, factor, factor)


def redo():
    global tiers_coords
    tiers_coords = tiers_representations(root, largeur_ecran*0.55, hauteur_ecran*0.7)
    canva.delete("all")
    add_liens(canva)
    place_tier()
    if aff_temps:
        label_temps()

def recentrer():
    redo()
    chemin()

def refaire_graphe():
    global tab_predecesseurs
    global reseau
    reseau = Graphe_list().reseaux
    _, tab_predecesseurs = algo_de_Floyd_Warshall(matrice_graphe(reseau))
    redo()

def afficher_temps():
    global aff_temps
    if aff_temps:
        canva.delete('temps')
        aff_temps = False
    else:
        label_temps()
        aff_temps = True

def label_temps():
    update_coords()
    temps = []
    for i in range(len(reseau)):
            for j in range(len(reseau[i].parents)):
                x = (tiers_coords[i][0]+tiers_coords[reseau[i].parents[j]][0]*5)/6
                y = (tiers_coords[i][1]+tiers_coords[reseau[i].parents[j]][1]*5)/6
                while (x, y) in temps:
                    x *= 1.1
                    y *= 1.1
                temps.append((x, y))
                canva.create_text(x, y, text= reseau[i].temps[j], tags='temps')

def update_coords():
    for i in range(len(tiers)):
        x, y = canva.coords(tiers[i][1])
        tiers_coords[i] = (x, y)  


def chemin():
        update_coords()
        debut = int(points[0].get())
        fin = int(points[1].get())
        chemin = chemin_le_plus_court(debut, fin, tab_predecesseurs)
        temps_tot = temps_le_plus_court(reseau, chemin)
        canva.delete("chemin")
        for i in range(len(chemin)-1) :
            canva.create_line(
                tiers_coords[chemin[i]][0],
                tiers_coords[chemin[i]][1],
                tiers_coords[chemin[i+1]][0],
                tiers_coords[chemin[i+1]][1],
                fill="black",
                width=2.5,
                tags="chemin")
        res.config(text = f'Le chemin le plus court de {debut} à {fin} est\n'+
                    f'{" -> ".join(map(str, chemin))}\n'+
                    f'de temps total {temps_tot}')
        


"""Bouttons"""

def titre(couleur):
    textes = [["Voici notre grand secret :", 20],
              ["Topologie d'interconnexion de 100 noeuds", 20],
              ["(Magnifique n'est-ce pas ? :) on peut même le déplacer et le zoomer !)", 15],
              ["Tu peux retrouver le chemin le plus court entre deux noeuds !", 20]]

    for t in textes:
        l = tk.Label(root, text= t[0], font=("Courier New", t[1]),  
                     justify='center', background = couleur, 
                     fg = text_couleur)
        l.pack()


def choisir_noeuds_t(frame):
    f = tk.Frame(frame, background= couleur, borderwidth = 0)
    f.grid(row = 0, pady= 40)
    textes = [["Allez essaye ;)", 20, 's'],
              ["Choisis deux valeurs entre 0 et 99", 15, 'w'],]
    
    for i in range(len(textes)):
        l = tk.Label(f, text= textes[i][0], font=("Courier New", textes[i][1]),  
                     justify='center', background = couleur, 
                     fg = text_couleur)
        l.grid(row = i, column = 0, sticky = textes[i][2])
            
def choisir_noeuds_v(frame):
    global points
    f = tk.Frame(frame, background= couleur, borderwidth = 0)
    f.grid(row = 1, pady= 10)
    textes = ["Noeud de départ :",
              "Noeud de d'arrivée :"]
    points = []

    for i in range(len(textes)):
        l = tk.Label(f, text= textes[i], font=("Courier New", 15),  
                     justify='center', background = couleur,
                     fg = text_couleur)
        l.grid(row = i, column = 0, sticky = 'w')
        val = tk.Entry(f)
        val.grid(row = i, column = 1)
        points.append(val)
    
    valider = tk.Button(f, text="Valider", bg = couleur, 
                        font=("Courier New", 15), fg = text_couleur,
                        command= chemin)
    valider.grid(row = 2, column = 0, sticky = 'w', pady= 40)


def choisir_noeuds(frame):
    choisir_noeuds_t(frame)
    choisir_noeuds_v(frame)


def redo_buttons(frame, couleur):
    textes = [["Recentrer le graphe", recentrer], 
              ["Refaire graphe", refaire_graphe],
              ['Afficher temps', afficher_temps]]
    redo_b = []
    for i in range(len(textes)):
        bouton = tk.Button(frame, 
                                 text= textes[i][0], 
                                 bg = couleur, 
                                 font=("Courier New", 12),
                                 fg = text_couleur, command= textes[i][1])
        bouton.grid(row = 0, column = i, padx = 5)
        redo_b.append(bouton)



"""Main"""


def main():
    global canva
    global root
    global tiers_coords
    global tiers
    global couleur
    global text_couleur
    global reseau
    global aff_temps
    global tab_predecesseurs
    global res
    global largeur_ecran
    global hauteur_ecran

    couleur = "#EDF9EE"
    text_couleur = "#041023"
    reseau = Graphe_list().reseaux
    aff_temps = False
    _, tab_predecesseurs = algo_de_Floyd_Warshall(matrice_graphe(reseau))
    print(tab_predecesseurs)


    root = tk.Tk()
    root.title('Algo des graphes')
    largeur_ecran = root.winfo_screenwidth()
    hauteur_ecran = root.winfo_screenheight()
    root.geometry(f"{largeur_ecran}x{hauteur_ecran}")
    root.configure(bg = couleur)

    
    #root.update_idletasks() 
    canva = tk.Canvas(root, width = largeur_ecran*0.55, 
                      height = hauteur_ecran*0.7, bg = couleur)
    canva.place(relx = 0.01, rely = 0.2)

    tiers = []
    tiers_coords = tiers_representations(root, largeur_ecran*0.55, hauteur_ecran*0.7)
    add_liens(canva)
    place_tier()

    titre(couleur)
    frame1 = tk.Frame(root, background= couleur, borderwidth = 0)
    frame1.place(relx = 0.6, rely = 0.30)
    choisir_noeuds(frame1)
    res = tk.Label(frame1, text= "", font=("Courier New", 15),  
                     justify='center', background = couleur,
                     fg = text_couleur)
    res.grid(row = 2)

    frame2 = tk.Frame(root, background= couleur, borderwidth = 0)
    frame2.place(relx = 0.6, rely = 0.85)
    redo_buttons(frame2, couleur)

    #root.bind("<Configure>", place_tier)
    canva.bind("<MouseWheel>", do_zoom)
    canva.bind('<ButtonPress-1>', lambda event: canva.scan_mark(event.x, event.y))
    canva.bind("<B1-Motion>", lambda event: canva.scan_dragto(event.x, event.y, gain=1))
    root.mainloop()

main()
