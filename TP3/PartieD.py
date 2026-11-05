from PartieA import Livre, Utilisateur  # On importe les classes de base
from PartieC import Bibliotheque  # On importe la classe Bibliotheque avec la gestion CSV

def afficher_menu():
    print("MENU BIBLIOTHEQUE")  # On affiche le titre du menu
    print("1. Ajouter un livre")  # On affiche la premiere option
    print("2. Ajouter un utilisateur")  # On affiche la deuxieme option
    print("3. Emprunter un livre")  # On affiche la troisieme option
    print("4. Rendre un livre")  # On affiche la quatrieme option
    print("5. Afficher les livres")  # On affiche la cinquieme option
    print("6. Quitter et sauvegarder")  # On affiche l'option de sortie

if __name__ == "__main__":
    b = Bibliotheque()  # On créer la bibliotheque
    b.charger_csv("livres.csv")  # On charge les donnees sauvegardees au lancement

    en_cours = True  # On initialise la variable pour maintenir la boucle active

    while en_cours:
        afficher_menu()  # On affiche le menu a chaque tour de boucle
        choix = input("Votre choix (1-6) : ")  # On recupere le choix de l'utilisateur

        if choix == "1":
            titre = input("Titre du livre : ")  # On demande le titre du livre à l'utilisateur
            auteur = input("Auteur du livre : ")  # On demande l'auteur du livre
            annee_str = input("Annee de parution : ")  # On demande l'annee en texte

            try:
                annee = int(annee_str)  # On tente de convertir l'annee en entier
                l = Livre(titre, auteur, annee)  # On cree l'objet Livre
                b.ajouter_livre(l)  # On ajoute le livre dans la bibliotheque
                print("Livre ajoute avec succes !")  # On confirme l'ajout
            except ValueError:
                print("Erreur : L'annee doit etre un nombre entier.")  # On gere le cas ou l'annee n'est pas un nombre

        elif choix == "2":
            nom = input("Nom de l'utilisateur : ")  # On demande le nom de l'utilisateur
            u = Utilisateur(nom)  # On cree l'objet Utilisateur
            b.ajouter_utilisateur(u)  # On ajoute l'utilisateur dans la bibliotheque
            print("Utilisateur ajoute avec succes !")  # On confirme l'ajout en affichant

        elif choix == "3":
            nom = input("Nom de l'utilisateur : ")  # On demande le nom de l'emprunteur
            titre = input("Titre du livre : ")  # On demande le titre du livre a emprunter
            b.emprunter(nom, titre)  # On tente de faire l'emprunt

        elif choix == "4":
            nom = input("Nom de l'utilisateur : ")  # On demande le nom de la personne qui rend
            titre = input("Titre du livre : ")  # On demande le titre du livre a rendre
            b.rendre(nom, titre)  # On tente de rendre le livre

        elif choix == "5":
            b.afficher_livres()  # On affiche la liste des livres de la bibliotheque

        elif choix == "6":
            b.sauvegarder_csv("livres.csv")  # On sauvegarde l'etat dans le fichier CSV
            print("Donnees sauvegardees!")  # On affiche le message de fin
            en_cours = False  # On passe la variable a False pour quitter la boucle

        else:
            print("Choix invalide ! Veuillez saisir un nombre entre 1 et 6.")  # On gere les choix incorrects