#Partie Antoine:
    
import tkinter as tk
import random as rd


def verif(b):
    # Vérifie si le bouton cliqué est adjacent au bouton0
    pos3 = bouton0.grid_info()
    pos4 = b.grid_info()
    if (pos4["row"] == pos3["row"] + 1) and (pos4["column"] == pos3["column"]) :
        echange_pos(b)

    elif (pos4["row"] == pos3["row"] - 1) and (pos4["column"] == pos3["column"]) :
        echange_pos(b)

    elif (pos4["column"] == pos3["column"] + 1) and (pos4["row"] == pos3["row"]) :
        echange_pos(b)

    elif (pos4["column"] == pos3["column"] - 1) and (pos4["row"] == pos3["row"]) :
        echange_pos(b)


def echange_pos(b):
    # récupère les informations de placement des widgets
    pos1 = bouton0.grid_info()
    pos2 = b.grid_info()

    # échange les positions des widgets
    bouton0.grid(row=pos2["row"], column=pos2["column"])
    b.grid(row=pos1["row"], column=pos1["column"])

    win(boutons)


# renvoie un message si le joueur gagne
def win(boutons):
    if ((boutons[0].grid_info()["row"] == 0 and boutons[0].grid_info()["column"] == 0) and 
        (boutons[1].grid_info()["row"] == 0 and boutons[1].grid_info()["column"] == 1) and
        (boutons[2].grid_info()["row"] == 0 and boutons[2].grid_info()["column"] == 2) and 
        (boutons[3].grid_info()["row"] == 0 and boutons[3].grid_info()["column"] == 3) and 
        (boutons[4].grid_info()["row"] == 1 and boutons[4].grid_info()["column"] == 0) and 
        (boutons[5].grid_info()["row"] == 1 and boutons[5].grid_info()["column"] == 1) and 
        (boutons[6].grid_info()["row"] == 1 and boutons[6].grid_info()["column"] == 2) and 
        (boutons[7].grid_info()["row"] == 1 and boutons[7].grid_info()["column"] == 3) and
        (boutons[8].grid_info()["row"] == 2 and boutons[8].grid_info()["column"] == 0) and
        (boutons[9].grid_info()["row"] == 2 and boutons[9].grid_info()["column"] == 1) and
        (boutons[10].grid_info()["row"] == 2 and boutons[10].grid_info()["column"] == 2) and
        (boutons[11].grid_info()["row"] == 2 and boutons[11].grid_info()["column"] == 3) and
        (boutons[12].grid_info()["row"] == 3 and boutons[12].grid_info()["column"] == 0) and
        (boutons[13].grid_info()["row"] == 3 and boutons[13].grid_info()["column"] == 1) and
        (boutons[14].grid_info()["row"] == 3 and boutons[14].grid_info()["column"] == 2)):
        
        label = tk.Label(fen, text="Bravo! Victoire!", fg = "red2", font = ("helvetica", "30"))
        label.grid(row=4, column=0, columnspan=4)


#création de la fenêtre
fen = tk.Tk()
fen.title("Jeu taquin")

# création des boutons à des places aléatoire
pos = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2)]

boutons = []
for i in range(15):
    row, column = rd.choice(pos)
    pos.remove((row, column))
    bouton = tk.Button(fen, bg="dark goldenrod", text=f"{i+1}", anchor="center", height=3,
                        width=7, font=("helvitica", "20"))
    bouton.grid(row=row, column=column)
    bouton.config(command=lambda b=bouton: verif(b))
    boutons.append(bouton)

# création du bouton0
bouton0 = tk.Button(fen, bg="floral white", height=3, width=7, font=("helvitica", "20"))
bouton0.grid(row=3, column=3)

fen.mainloop()
