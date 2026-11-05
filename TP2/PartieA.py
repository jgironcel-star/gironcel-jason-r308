# Jeu d'essai
class Grille:
    def __init__(self):
        # permet de faire une grille 3x3 remplie d'espaces " "
        self.grille = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
    def afficher(self):
        for i in range(3): # boucle pour parcourir les 3 lignes de la grille         
            print(" " + " | ".join(self.grille[i]) + " ") #Permet d'écrire le tableau, la fonction .join permet d'assembler les éléments de la ligne avec "|"
            if i < 2: #Permet l'affichage d'un séparateur après les 2 premières lignes.
                print("-----------")
    def jouer(self, x, y, joueur):
        if x < 0 or x > 2 or y < 0 or y > 2:    #Vérification des coordonnées hors grille
            print("Coordonnées inccorrecte (hors grille)")
            return False
            
        #Vérification si la case est déjà occupée
        if self.grille[x][y] != " ": #On veérifie si self.grille[x][y] est différent d'une case vide, si elle est différente cela veut dire que la case est déjà occupée.
            print("Cette case est déjà occupée")
            return False
            
        self.grille[x][y] = joueur #Placement du pion dans la grille
        return True
    
    def est_gagnant(self,j):
        for i in range(3):
            if self.grille[i][0]==j and self.grille[i][1]==j and self.grille[i][2]==j: #Vérifcation qu'il y a 3 symboles identiques sur la meme ligne. 
                return True
            for i in range(3):
                        if self.grille[0][i]==j and self.grille[1][i]==j and self.grille[2][i]==j: #Vérifcation qu'il y a 3 symboles identiques sur la meme colonne. 
                            return True
        for i in range(3):
             if self.grille[2][0] == j and self.grille[1][1] == j and self.grille[0][2] == j: #Vérification qu'il y a 3 symboles identiques sur la diagonale montante.
                  return True
        for i in range(3):
             if self.grille[2][2] == j and self.grille[1][1] == j and self.grille[0][0] == j: #Vérification qu'il y a 3 symboles identiques sur la diagonale descendante.
                  return True
        return False  #Si aucune des conditions est respecté , donc si aucun alignement est respecté , on retourne False.

    def est_plein(self):
         for ligne in self.grille: #boucle qui parcourt chaque ligne de la grille.
              for case in ligne: # On parcout chaque case de la ligne 
                if case == " ":#Si on trouve au moins une case contenant un espace (" "), la grille n'est pas pleine
                    return False
         return True #Si les 2 boucles se sont terminées ssans trouver d'espace, toutes les cases sont pleines,occupées.
#Jeu d'essai de la Partie A
g = Grille()
g.jouer(0, 0, "X"); g.jouer(0, 1, "O"); g.jouer(1, 1, "X")
g.afficher()
# Tests d'erreurs
g.jouer(0, 0, "O")  # Refusé (occupée)
g.jouer(3, 0, "O")  # Refusé (hors grille)
# Tests de victoire
print("X gagnant ? ->", g.est_gagnant("X"))  # False
g.jouer(2, 2, "X") # Complète la diagonale
g.afficher()
print("X gagnant après (2,2) ? ->", g.est_gagnant("X"))# True