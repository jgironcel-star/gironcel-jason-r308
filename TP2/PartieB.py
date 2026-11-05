import random #On importe la fonction random pour la classe JoueurIA,pour tirer un coup au hasard.
class JoueurHumain:
    def prochain_coup(self , grille , symbole):
        x=int(input("Veuillez entrer la ligne (0, 1 ou 2) : ")) #Permet à l'utilisateur de saisir une coordonnée pour la ligne . Le "int" permet de convertir la valeur en entier 
        y=int(input("Entrez la colonne (0, 1 ou 2) : "))        #permet à l'utilisateur de saisir une coordonnée pour la colonne .
        return (x,y) #Retourne les coordonnées x et y sous forme d'un tuple.
class JoueurIA:
    def prochain_coup(self , grille , symbole):
        cases_libres=[]#On créer une liste vide
        for x in range(0,3): #On fait 2 boucles imbriquées, la première boucle permet de parcourir les lignes de la grille donc de 0 à 2.
            for y in range(0,3): #La deuxième boucle parcourt les colonnes de la grille de 0 à 2aussi .
                if grille.grille[x][y] == " ": #On teste pour savoir si il y a des cases de disponibles donc des cases vides.
                    cases_libres.append((x,y)) #On ajoute les coordonnées sous forme de tuple à la liste .
        return random.choice(cases_libres)#Permet de choisir aléatoirement une case dans la liste cases_libres.
