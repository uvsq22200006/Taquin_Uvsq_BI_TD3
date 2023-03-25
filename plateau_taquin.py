import random

valeurs = list(range(1, 16))
random.shuffle(valeurs)

plateau = [[valeurs.pop() if valeurs else " " for j in range(4)] for i in range(4)]
plateau[3][3] = " "

for lignes in plateau:
    print(lignes)

   
Partie Antoine:
    
import tkinter as tk
import random as rd

# fonction qui permet d'échanger la position du bouton cliqué avec le bouton0
def echange_pos(b):

    # récupère les informations de placement des boutons
    pos1 = bouton0.grid_info()
    pos2 = b.grid_info()
    
    # échange les positions des boutons
    bouton0.grid(row=pos2['row'], column=pos2['column'])
    b.grid(row=pos1['row'], column=pos1['column'])

# création de la fenêtre
fen = tk.Tk()
fen.title("Jeu taquin")

# position possible dans la grille
pos = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)]

# création des boutons sauf le bouton0
for i in range(8):
    row, column = rd.choice(pos) # on choisit les coordonnées parmis "pos"
    pos.remove((row, column))  # Enlever les coordonnées choisies de la liste des positions restantes
    bouton = tk.Button(fen, bg = "dark goldenrod", text=f"{i+1}", anchor = "center", height = 3,
                        width = 7, font = ("helvitica", "20")) # création des boutons et de leur texte
    bouton.grid(row=row, column=column) # position des boutons
    bouton.config(command=lambda b=bouton: echange_pos(b)) # commande des boutons qui renvoie à la fonction "echange_pos"

# création du bouton0 aux coordonnées (2,2)
bouton0 = tk.Button(fen, bg = "floral white", anchor = "center", height = 3, width = 7,
                     font = ("helvitica", "20"))
bouton0.grid(row = 2, column = 2)

# affichage de la fenêtre
fen.mainloop()
