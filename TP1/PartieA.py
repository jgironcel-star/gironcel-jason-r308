etudiants = {}  #Création d'un dictionnaire vide

def ajouter_etudiant(d, nom ,note): #Création de la fonction ajouter étudiant
    d[nom] = float(note) #Ajout de la clé nom et de la valeur note au dictionnaire d.


def moyenne_classe(d):
    somme =0  #Initailisation de la variable somme à 0
    if len(d) == 0: # Permet de vérifier si le dictionnaire est vide
        return 0.0
    for notes in d.values(): #BOucle qui permet de parcourir les notes (qui sont des valeurs) dans le dictionnaire.
        somme = somme + notes  #Permet d'additoner toutes les notes récupérées
    moyenne = somme/len(d) #calcule la moyenne en faisant la somme divisée par la longueur du tableau (le nombre de notes total)
    return moyenne

def meilleur_etudiant(d):
    if len(d) == 0: #Verifie si le dictionnaire est vide , sil il est vide il renvoie un tuple avec des variables None(rien).
        return (None , None)
    meilleur_note = -1 #Initialisatioin de varible meilleur_note à -1 au cas ou les notes du dictionnaire seraient égales à 0.
    meilleur_nom = None # initialisation de la variable meilleur_nom . Cette variable c'est rien pour l'instant (None).
    for nom , note in d.items(): #Boucle qui permet de parcourir le noms et les notes dans le dictionnaire.
        if note > meilleur_note: 
            meilleur_note = note #la variable meilleur_note prends la valeur de note
            meilleur_nom = nom #Prends la valeur du premier nom (avec la note la plus élevée).
    return (meilleur_nom,meilleur_note)

def sauvegarder_fichier(d , nom_fichier):
    with open(nom_fichier, "w", encoding="utf-8") as f: #ligne permettant d'ouvrir le fichier passé en paramètre et d'écrire dans ce fichier ("w" permet d'écrire dans un fichier)
        for nom , note in d.items(): #parcourt les noms et les notes du dictionnaire
            f.write(f"{nom}:{note}\n") # écrit les noms et note dans le fichier

#Gestion des erreurs:
def charger_fichier(nom_fichier):
    d = {} # Dictionnaire qui contiendra les données chargées
    
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:  # EEssai d'ouvrir le fichier en mode lecture ("r") avec l'encodage UTF-8
            for ligne in f:
                ligne = ligne.strip()  # Retire les espaces inutiles et les retours à la ligne (\n)
                
                if ":" in ligne:#Vérification que la ligne contient bien le séparateur ":"
                    
                    nom, note_str = ligne.split(":", 1) # Découpe la ligne au premier ":" sépare le nom et la note
                    
                    try:
                        # Essai de convertir le texte de la note en float
                        d[nom] = float(note_str)
                    except ValueError:
                        # Si la conversion échoue (ex: la note est "quinze" au lieu de 15),
                        # cette erreur est capturée : on affiche un avertissement et le programme continue sans planter
                        print(f"Ligne ignorée (note invalide) : {ligne}")

    except FileNotFoundError:
        # Si le fichier n'existe pas lors du open(), cette erreur est capturée :
        # on affiche un message clair au lieu de faire planter le script avec un crash Python
        print("Fichier non trouvé. Un dictionnaire vide est renvoyé.")
    
    # On renvoie le dictionnaire (qu'il soit plein, partiellement rempli ou vide)
    return d

#Jeu d'essai:
etudiants = {}
#Appel des différentes fonctions pour tester le code .
ajouter_etudiant(etudiants, "Alice", 12)
ajouter_etudiant(etudiants, "Bob", 15)
ajouter_etudiant(etudiants, "Claire", 9.5)

print("Moyenne :", moyenne_classe(etudiants))
print("Meilleur :", meilleur_etudiant(etudiants))

sauvegarder_fichier(etudiants, "notes.txt")
etudiants_charges = charger_fichier("notes.txt")
print("Chargé :", etudiants_charges)