import random #on importe le random pour pouvoir effectuer des tirages aléatoires
from PartieA import Grille
from PartieB import JoueurHumain, JoueurIA
def jouer_partie(j1, j2):
    grille = Grille() # Créaation de la grille de jeu en reprenant la la class Grille() faite dans la partie A
    joueurs = [j1, j2]  # Création d'une liste des deux joueurs
    symboles = ["X", "O"]  # Création d'une liste des deux symboles , "X" pour j1 et "O" pour j2

    index_courant = 0  # Index pour savoir quel joueur doit jouer (0 pour J1, 1 pour J2)
    en_cours = True  # Variable pour maintenir la boucle de jeu active
    while en_cours:
        joueur_actuel = joueurs[index_courant]
        symbole_actuel = symboles[index_courant]

        grille.afficher()   # Affichage de la grille au début du tour
        print("Tour du joueur", symbole_actuel)

        x, y = joueur_actuel.prochain_coup(grille, symbole_actuel)   # Récupération des coordonnées via la méthode du joueur actuel
        coup_valide = grille.jouer(x, y, symbole_actuel)   # Tentative de placement du pion dans la grille
        if coup_valide:
            # Test si le joueur actuel aligne 3 symboles
            if grille.est_gagnant(symbole_actuel):   # Test si le joueur actuel aligne 3 symboles en récupérant la fonction est_gagnant de la partie A
                grille.afficher()
                print("Le joueur", symbole_actuel, "a gagne !")
                en_cours = False
                return symbole_actuel
            
            elif grille.est_plein():  # Test si la grille est pleine grâce a la fonction est_plein ecrit dans la partie A
                grille.afficher()
                print("Match nul ! La grille est pleine.")
                en_cours = False
                return "NUL"
            else:
                index_courant = 1 - index_courant # Passage au joueur suivant (si 0 devient 1, si 1 devient 0)
        else:
            print("Coup invalide ! Veuillez rejouer.") # Si le coup est refuse, le même joueur rejoue au tour suivant
#Jeu d'essai : 20 parties IA vs IA
if __name__ == "__main__":
    ia1 = JoueurIA()
    ia2 = JoueurIA()

    print("TEST 20 PARTIES IA vs IA")
    victoires_x = 0
    victoires_o = 0
    matchs_nuls = 0

    for i in range(20):  #Boucle permettant de faire les 20 parties
        print("--- Partie", i + 1, "---") 
        resultat = jouer_partie(ia1, ia2)
        if resultat == "X":
            victoires_x = victoires_x + 1
        elif resultat == "O":
            victoires_o = victoires_o + 1
        else:
            matchs_nuls = matchs_nuls + 1

    print("BILAN DES 20 PARTIES")
    print("Victoires X :", victoires_x)
    print("Victoires O :", victoires_o)
    print("Matchs nuls :", matchs_nuls)