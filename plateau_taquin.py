import random

valeurs = list(range(1, 16))
random.shuffle(valeurs)

plateau = [[valeurs.pop() if valeurs else " " for j in range(4)] for i in range(4)]
plateau[3][3] = " "

for lignes in plateau:
    print(lignes)
