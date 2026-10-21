import random #Le module random permet de choisir une variable de façon aléatoire
def nombre_a_deviner():
    nombre_secret = random.randint(1, 100) #Génération du nombre secret entre 1 et 100 inclus
    essai_max = 10 # Nombre d'essais maximum autorisés
    essai = 1      # Initialisation du compteur d'essais à 1
    while essai <= essai_max: # Boucle de jeu tant que le nombre d'essais autorisé n'est pas dépassé
        nombre = int(input("Entrez un nombre : ")) #Demande de la saisie d'un nombre à l'utilisateur
        if nombre < nombre_secret:
            print("Trop petit")
            essai = essai + 1  #Ajout d'un essai au compteur 
        elif nombre > nombre_secret:
            print("Trop grand")
            essai = essai + 1  #Ajout d'un essai au compteur
        else:
            print("Gagné")
            break  # Ajout du break pour stopper la boucle dees que le joueur à gagné
    if essai > essai_max: # Vérification de la défaite:exécuté seulement si les 10 essais ont été épuisés
        print(f"Perdu, le nombre secret est {nombre_secret}")   
#Test du jeu:
nombre_a_deviner() #Appel de la fonction pour tester le jeu
