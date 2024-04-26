import tkinter as tk
from PIL import Image, ImageTk

couleur = "beige"

connex = tk.Tk()
connex.title("Interface")
largeur_ecran = connex.winfo_screenwidth()
hauteur_ecran = connex.winfo_screenheight()
connex.geometry(f"{largeur_ecran}x{hauteur_ecran}")
connex.configure(bg=couleur)

def btnnext():
    connex.destroy()
    import routage

btnnext= tk.Button(connex, text="prochaine étape", bg = couleur, command=btnnext, font=("Courier New", 10))
btnnext.place(relx=0.85, rely=0.1, anchor='n')


connex.mainloop()

