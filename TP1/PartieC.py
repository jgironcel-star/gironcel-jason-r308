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
#Appel des différentes fonctions par des variables et affichage des résultats.
manip_mot = choisir_mot(liste)
print(manip_mot)
resultat_masque = masque(manip_mot)
print(resultat_masque)

