import tkinter as tk
from PIL import Image, ImageTk
from data import couleur, text_couleur

"""Page d'acceil"""


racine = tk.Tk()
racine.title("Interface")
largeur_ecran = racine.winfo_screenwidth()
hauteur_ecran = racine.winfo_screenheight()
racine.geometry(f"{largeur_ecran}x{hauteur_ecran}")
racine.configure(bg=couleur)

def btncestparti():
    racine.destroy()
    import interface

label_message = tk.Label(racine, text="Projet IN403",font=("Courier New", 50),  
                         justify='center', background=couleur, fg = text_couleur)
label_message2 = tk.Label(racine, text="Algorithmique des Graphes",font=("Courier New", 50),  
                          justify='center', background=couleur, fg = text_couleur)
label_message3 = tk.Label(racine, text="Par les reines du monde Daria, Vanessa, Maïlys et Maryatou",
                          font=("Courier New", 15), background=couleur, fg = text_couleur)
label_message5 = tk.Label(racine, text="Pour notre cher professeur Thierry Mots-Tort ",
                          font=("Courier New", 15), background=couleur, fg = text_couleur)
label_message4 = tk.Label(racine, text="2023/2024",font=("Courier New", 15), 
                          background=couleur, fg = text_couleur)
bouton = tk.Button(racine, text="Que l'aventure commence!")
label_message.pack()
label_message2.pack()
label_message3.place(relx=0.5, rely=0.85, anchor='s')
label_message5.place(relx=0.5, rely=0.9, anchor='s')
label_message4.place(relx=0.9, rely=0.9, anchor='s')

bouton_page_suivante = tk.Button(racine, text="Commençons l'aventure!",command=btncestparti, background=couleur, font=("Courier New", 15))
bouton_page_suivante.place(relx=0.5, rely=0.75, anchor='s')

imgori = Image.open("nvgraphe.png")
image = imgori.resize((300,300), Image.ANTIALIAS)
image_tk = ImageTk.PhotoImage(image)  
img = tk.Label(racine, image=image_tk, bg=couleur)
img.place(relx=0.5, rely= 0.65, anchor='s')

racine.mainloop()