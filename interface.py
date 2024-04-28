import tkinter as tk
from tiers_representation_geom import tiers_representations
from data import *
from create_graph import Graphe_list


def tier(color, nb, coords):
    #global circle_size
    #circle_size /= 2
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
    
    color =  data_tier1.color
    for j in range(len(tiers_coords)):
        tier(color, j, tiers_coords[j])
        if j == data_tier1.n-1:
            color = data_tier2.color
        elif j == data_tier2.n+data_tier1.n-1:
            color = data_tier3.color

def add_liens(canva):
    reseau = Graphe_list().reseaux
    color =  data_tier3.color

    for i in reversed(range(len(reseau))):
        for j in range(len(reseau[i].parents)):
            canva.create_line(tiers_coords[i][0], tiers_coords[i][1], 
                              tiers_coords[reseau[i].parents[j]][0], tiers_coords[reseau[i].parents[j]][1],
                              fill = color)
            
            #x_l = (tiers_coords[i][0]+ tiers_coords[j][0])/2
            #y_l = (tiers_coords[i][1]+ tiers_coords[j][1])/2
            #canva.create_text(x_l, y_l, text = reseau[i].temps[j])

        if i == data_tier1.n:
            color = data_tier1.color
        elif i == data_tier2.n+data_tier1.n:
            color = data_tier2.color

    
def do_zoom(event):
    x = canva.canvasx(event.x)
    y = canva.canvasy(event.y)
    factor = 1.001 ** event.delta
    canva.scale(tk.ALL, x, y, factor, factor)
    #for t in tiers:
        #t.place_configure(x = x, y = y)
        #t.scale(x = x, y = y)
    #print(x, y, factor)
    #new_coords = tiers_representations(root, (x, y), factor)
    #for i in range(len(tiers)):
    #    tiers[i].place_configure(x = new_coords[i][0], y = new_coords[i][1])
    #resize_tiers(factor)

def nextpage():
    root.destroy()
    import connexite

def main():
    global canva
    global root
    global tiers_coords
    global tiers
    global circle_size

    root = tk.Tk()
    root.title('Algo des graphes')
    largeur_ecran = root.winfo_screenwidth()
    hauteur_ecran = root.winfo_screenheight()
    root.geometry(f"{largeur_ecran}x{hauteur_ecran}")
    root.configure(bg="beige")

    couleur = "beige" 

    
    root.update_idletasks() 
    canva = tk.Canvas(root, width=root.winfo_width(), height = 600, bg=couleur)
    canva.place(relx = 0, rely = 0.2)

    tiers = []
    tiers_coords = tiers_representations(root)
    add_liens(canva)
    place_tier()

    l1= tk.Label(root, text="Première étape de l'aventure :",font=("Courier New", 30),  justify='center', background=couleur)
    l1.pack()
    l2= tk.Label(root, text="Topologie d'interconnexion de 100 noeuds",font=("Courier New", 30),  justify='center', background=couleur)
    l2.pack()
    l3= tk.Label(root, text="(Magnifique n'est-ce pas ? :) on peut même le déplacer et le zoomer !)",font=("Courier New", 15),  justify='center', background=couleur)
    l3.pack()
    marginbottom = tk.Canvas(root, width=largeur_ecran, height = 40, bg=couleur)
    marginbottom.place(relx = 0, rely=0.9)
    marginright = tk.Canvas(root, width=40, height=hauteur_ecran, bg=couleur)
    marginright.place(relx = 0.96, rely=0)
    marginleft = tk.Canvas(root, width=40, height=hauteur_ecran, bg=couleur)
    marginleft.place(relx = 0.001, rely=0)

    bouton_page_suivante = tk.Button(canva, text="Pret pour la prochaine étape ?",command=nextpage, background=couleur, font=("Courier New", 10))
    bouton_page_suivante.place(relx=0.85, rely=0.85, anchor='s')

    bouton_recentrer = tk.Button(canva, text="recentrer le graphe ", bg = couleur, font=("Courier New", 10))
    bouton_recentrer.place(relx=0.85, rely=0.1, anchor='n')
    
    #root.bind("<Configure>", place_tier)
    canva.bind("<MouseWheel>", do_zoom)
    canva.bind('<ButtonPress-1>', lambda event: canva.scan_mark(event.x, event.y))
    canva.bind("<B1-Motion>", lambda event: canva.scan_dragto(event.x, event.y, gain=1))
    root.mainloop()

main()
