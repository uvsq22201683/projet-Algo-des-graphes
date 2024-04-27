import tkinter as tk

# Fonction qui sera exécutée lorsque le bouton sera cliqué
def afficher_input():
    valeur_input = entry.get()
    print("La valeur saisie est :", valeur_input)

# Créer une instance de la classe Tk
root = tk.Tk()

# Créer un widget Entry
entry = tk.Entry(root)
entry.pack()  # Ajouter le widget Entry à la fenêtre

# Créer un bouton
bouton = tk.Button(root, text="Valider", command=afficher_input)
bouton.pack()  # Ajouter le bouton à la fenêtre

# Lancer la boucle principale
root.mainloop()
