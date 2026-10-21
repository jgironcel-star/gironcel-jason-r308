
import random  #Le module random permet de choisir une variable de façon aléatoire
liste = ["python", "code", "reseau", "securite"]
def choisir_mot(liste):
    mot_random = random.choice(liste)  #permet de choisir un mot de façon aléatoire dans la liste
    return mot_random.upper() #La fonction upper permet de mettre le chaque lettre du mot en majuscules
def masque(mot):
    m= []  #initialisation d'un tableau vide pour stocker ensuite les "_".
    for lettre in range(len(mot)): #boucle permettant de parcourir les lettres du mot
        m.append('_') #fonction append permettant d'ajouter le cacractère '_' à la liste m.
    return m
def reveler_lettre(mot, masque, lettre):
    for i in range(len(mot)): #parcourt chaque lettre du mot
        if mot[i] == lettre:
            masque[i] = lettre
    return masque
def pendu():
    mot_secret = choisir_mot(liste)  # On pioche un mot au hasard grâce à la fonctioin choisir_mot déjà faite dans la partie C
    masque_courant = masque(mot_secret)  # On crée la liste de '_' grâce à la fonction masque déjà faite dans la partie C
    erreurs = 0
    lettres_proposees = [] #Initialisation d'une liste vide pour stocker les lettres proposées.
    # La boucle tourne tant qu'on a moins de 7 erreurs et qu'il reste des '_'
    while erreurs < 7 and '_' in masque_courant:
        #Affichage simple du mot masqué
        affichage = ""
        for lettre in masque_courant: # Reconstitution d'une chaîne lisible avec un espace entre chaque caractère du masque
            affichage = affichage + lettre + " "
        
        print("\nMot à deviner :", affichage)
        print("Nombre d'erreurs :", erreurs, "/ 7") #Permet d'indiquer à l'utilisateur son nombre d'erreur dans le jeu (nombre d'erreurs limitées à 7)
        print("Lettres déjà essayées :", lettres_proposees)

        saisie = input("Proposez une lettre : ")#Demande d'une lettre à l'utilisateur
        lettre = saisie.upper()  # On met la lettre en majuscule grâce à la fonction upper.
        #on vérifie si la lettre est déja dans la liste des lettres déjà proposées.
        if lettre in lettres_proposees:
            print("Vous avez déjà essayé cette lettre !")
        else:
            lettres_proposees.append(lettre)  # Ajout de la lettre dans la liste des lettres proposées grâce à la fonction append
            if lettre in mot_secret:
                # La lettre est bonne on met à jour le masque
                masque_courant = reveler_lettre(mot_secret, masque_courant, lettre)
            else:
                # La lettre n'est pas dans le mot on a donc une erreur de plus
                erreurs = erreurs + 1
                print("Lettre absente !")
    #Fin du jeu
    if '_' not in masque_courant:
        print("\nGagné ! Le mot était bien :", mot_secret)
    else:
        print("\nPerdu... Le mot était :", mot_secret)
pendu()# Lancement du jeu

