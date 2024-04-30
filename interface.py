import tkinter as tk
from tiers_representation_geom import tiers_representations
from data import *
from create_graph import Graphe_list

"""Graph canvas"""

def tier(color, nb, coords):
    """Place un noeuds sur le canvas"""
    circle_size = 9
    x0 = coords[0]-circle_size
    y0 = coords[1]-circle_size
    x1 = coords[0]+circle_size
    y1 = coords[1]+circle_size
    t = canva.create_oval( x0, y0, x1, y1, outline = color, fill = 'white')
    t_label = canva.create_text(coords[0], coords[1], text= nb)
    tiers.append([t, t_label])

def place_tier():
    """Place les noeuds sur le canvas"""
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
    """Place les aretes sur le canvas"""
    color =  data_tier1.color
    width = 2
    for i in reversed(range(len(reseau.reseaux))):
        for j in range(len(reseau.reseaux[i].parents)):
            if reseau.reseaux[i].parents[j] < data_tier1.n:
                color =  data_tier1.color
                width = 2
            else: 
                color =  data_tier2.color
                width = 1

            canva.create_line(tiers_coords[i][0], tiers_coords[i][1], 
                              tiers_coords[reseau.reseaux[i].parents[j]][0], tiers_coords[reseau.reseaux[i].parents[j]][1],
                              fill = color, width = width)

def do_zoom(event):
    """Zoom du canvas"""
    x = canva.canvasx(event.x)
    y = canva.canvasy(event.y)
    factor = 1.001 ** event.delta
    canva.scale(tk.ALL, x, y, factor, factor)


"""Graph canvas actions"""

def redo():
    global tiers_coords
    tiers_coords = tiers_representations(root, largeur_ecran*0.55, hauteur_ecran*0.7)
    canva.delete("all")
    add_liens(canva)
    place_tier()
    if aff_temps:
        label_temps()

def recentrer():
    """Recentrer le graphe existant au sein d'un canvas"""
    redo()
    chemin()

def refaire_graphe():
    """Tracer un nouveau graphe"""

    global reseau
    reseau = Graphe_list()
    redo()


def label_temps():
    """Afficher les valeurs des aretes"""
    update_coords()
    temps = []
    center = [int(largeur_ecran/2), int(hauteur_ecran/2)+15]
    for i in range(len(reseau.reseaux)):
            for j in range(len(reseau.reseaux[i].parents)):
                if i < j:
                    x = (tiers_coords[reseau.reseaux[i].parents[j]][0] + tiers_coords[i][0]*5)/6
                    y = (tiers_coords[reseau.reseaux[i].parents[j]][1]+ tiers_coords[i][1]*5)/6
                else:
                    x = (tiers_coords[i][0]+tiers_coords[reseau.reseaux[i].parents[j]][0]*5)/6
                    y = (tiers_coords[i][1]+tiers_coords[reseau.reseaux[i].parents[j]][1]*5)/6
                while (x, y) in temps:
                    x *= 1.1
                    y *= 1.1
                temps.append((x, y))
                canva.create_text(x, y, text= reseau.reseaux[i].temps[j], 
                                  font=('Arial', 7), tags='temps')

def afficher_temps():
    """Afficher ou cacher les valeurs des aretes 
    quand le boutton est appuiye"""
    global aff_temps
    if aff_temps:
        canva.delete('temps')
        aff_temps = False
    else:
        label_temps()
        aff_temps = True


def update_coords():
    """Calcule les coordonnes des noeuds apres le zoom"""
    for i in range(len(tiers)):
        x, y = canva.coords(tiers[i][1])
        tiers_coords[i] = (x, y)  

def chemin():
    """Trace le plus court chemin sur le graphe"""
    update_coords()
    debut = int(points[0].get())
    fin = int(points[1].get())
    chemin = reseau.chemin_le_plus_court(debut, fin)
    #temps_tot = temps_le_plus_court(reseau, chemin)
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
                #f'de temps total {temps_tot}'+ 
                str(reseau.matrice_temps[debut][fin]))
        


"""Widgets"""

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
    global val
    val = []
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
        val.append(tk.Variable(f))
        val[-1].set('')
        val1 = tk.Entry(f, textvariable=val[-1])
        val1.grid(row = i, column = 1)
        points.append(val1)
    
    valider = tk.Button(f, text="Valider", bg = couleur, 
                        font=("Courier New", 15), fg = text_couleur,
                        command= chemin)
    valider.grid(row = 2, column = 0, sticky = 'w', pady= 40)


def choisir_noeuds(frame):
    """frame d'envoye de requettes"""
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

def choose_S(event):
    global actual_S_state
    x = event.x
    y = event.y
    for i in range(len(tiers)):
        t_coords = canva.coords(tiers[i][0])
        if (t_coords[0]< x <t_coords[2] or t_coords[0]> x >t_coords[2]) and \
        (t_coords[1]< y <t_coords[3] or t_coords[1]> y >t_coords[3]):
            break
    if actual_S_state == 0:
        val[0].set(str(i))
        actual_S_state = 1
    else:
        val[1].set(str(i))
        actual_S_state = 0
    

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
    global res
    global largeur_ecran
    global hauteur_ecran
    global actual_S_state
    global val

    reseau = Graphe_list()
    aff_temps = False
    actual_S_state = 0

    root = tk.Tk()
    root.title('Algo des graphes')
    largeur_ecran = root.winfo_screenwidth()
    hauteur_ecran = root.winfo_screenheight()
    root.geometry(f"{largeur_ecran}x{hauteur_ecran}")
    root.configure(bg = couleur)
    root.resizable(False,False)


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
    res = tk.Label(frame1, textvariable = "", font=("Courier New", 15),  
                     justify='center', background = couleur,
                     fg = text_couleur)
    res.grid(row = 2)

    frame2 = tk.Frame(root, background= couleur, borderwidth = 0)
    frame2.place(relx = 0.6, rely = 0.85)
    redo_buttons(frame2, couleur)

    canva.bind('<ButtonPress-3>', choose_S)
    canva.bind("<MouseWheel>", do_zoom)
    canva.bind('<ButtonPress-1>', lambda event: canva.scan_mark(event.x, event.y))
    canva.bind("<B1-Motion>", lambda event: canva.scan_dragto(event.x, event.y, gain=1))
    root.mainloop()

main()
