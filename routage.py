import tkinter as tk
from PIL import Image, ImageTk

couleur = "beige"

routage = tk.Tk()
routage.title("Interface")
largeur_ecran = routage.winfo_screenwidth()
hauteur_ecran = routage.winfo_screenheight()
routage.geometry(f"{largeur_ecran}x{hauteur_ecran}")
routage.configure(bg=couleur)

def btnnext():
    routage.destroy()
    import presentation

titre = tk.Label(routage, text="Table de routage de chaque noeud",font=("Courier New", 30),  justify='center', background=couleur)
titre.pack()

btnpro= tk.Button(routage, text="prochaine étape", bg = couleur, command=btnnext, font=("Courier New", 10))
btnpro.place(relx=0.5, rely=0.9, anchor='c')

routage.mainloop()

