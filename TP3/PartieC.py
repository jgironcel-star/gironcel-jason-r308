import csv  # On importe le module CSV de Python
from PartieA import Livre, Utilisateur  # On importe les classes de la Partie A

class Bibliotheque:
    def __init__(self):
        self.livres = {}  # On cree le dictionnaire pour les livres
        self.utilisateurs = {}  # On cree le dictionnaire pour les utilisateurs

    def ajouter_livre(self, livre):
        self.livres[livre.titre] = livre  # On associe le titre au livre

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs[utilisateur.nom] = utilisateur  # On associe le nom a l'utilisateur

    def emprunter(self, nom, titre):
        if nom in self.utilisateurs and titre in self.livres:  # On verifie que l'utilisateur et le livre existent
            u = self.utilisateurs[nom]  # On recupere l'objet utilisateur
            l = self.livres[titre]  # On recupere l'objet livre
            u.emprunter_livre(l)  # On effectue l'emprunt
        else:
            print("Erreur : Nom ou titre inconnu.")  # On affiche un message d'erreur si inconnu

    def rendre(self, nom, titre):
        if nom in self.utilisateurs and titre in self.livres:  # On verifie l'existence de l'utilisateur et du livre
            u = self.utilisateurs[nom]  # On recupere l'objet utilisateur
            l = self.livres[titre]  # On recupere l'objet livre
            u.rendre_livre(l)  # On rend le livre
        else:
            print("Erreur : Nom ou titre inconnu.")  # On affiche un message d'erreur si inconnu

    def sauvegarder_csv(self, nom_fichier):
        fichier = open(nom_fichier, "w", newline="", encoding="utf-8")  # On ouvre le fichier en ecriture
        writer = csv.writer(fichier)  # On cree l'objet writer pour le CSV
        for livre in self.livres.values():  # On parcourt la liste des livres
            emprunteur = livre.emprunteur  # On recupere le nom de l'emprunteur
            if emprunteur == None:  # On teste si le livre n'a pas d'emprunteur
                emprunteur = "Aucun"  # On indique Aucun si la case est vide
            writer.writerow([livre.titre, livre.auteur, livre.annee, livre.disponible, emprunteur])  # On ecrit la ligne
        fichier.close()  # On ferme le fichier CSV

    def charger_csv(self, nom_fichier):
        try:
            fichier = open(nom_fichier, "r", encoding="utf-8")  # On ouvre le fichier en lecture
            reader = csv.reader(fichier)  # On cree le lecteur CSV
            for ligne in reader:  # On parcourt chaque ligne du fichier
                if len(ligne) == 5:  # On verifie que la ligne contient bien les 5 elements
                    titre = ligne[0]  # On recupere le titre
                    auteur = ligne[1]  # On recupere l'auteur
                    annee = int(ligne[2])  # On convertit l'annee en entier
                    disponible = (ligne[3] == "True")  # On recupere le booleen de disponibilite
                    emprunteur = ligne[4]  # On recupere le nom de l'emprunteur
                    l = Livre(titre, auteur, annee)  # On cree l'objet Livre
                    self.ajouter_livre(l)  # On ajoute le livre dans la bibliotheque
                    if disponible == False and emprunteur != "Aucun":  # On verifie si le livre etait emprunte
                        if emprunteur not in self.utilisateurs:  # On verifie si l'utilisateur n'existe pas encore
                            u = Utilisateur(emprunteur)  # On cree l'utilisateur
                            self.ajouter_utilisateur(u)  # On ajoute l'utilisateur dans la bibliotheque
                        self.emprunter(emprunteur, titre)  # On retablit l'emprunt du livre
            fichier.close()  # On ferme le fichier
        except FileNotFoundError:
            print("Fichier non trouve, creation d'une bibliotheque vide.")  # On gere l'absence de fichier
#Jeu d'essai de la Partie C
if __name__ == "__main__":
    b1 = Bibliotheque()  # On instancie la premiere bibliotheque
    l1 = Livre("1984", "Orwell", 1949)  # On cree le livre 1984
    u1 = Utilisateur("Ana")  # On cree l'utilisateur Ana

    b1.ajouter_livre(l1)  # On ajoute 1984 a la bibliotheque 1
    b1.ajouter_utilisateur(u1)  # On ajoute Ana a la bibliotheque 1
    b1.emprunter("Ana", "1984")  # On fait emprunter 1984 par Ana

    b1.sauvegarder_csv("livres.csv")  # On sauvegarde dans le fichier CSV
    print("Donnees sauvegardees dans livres.csv")  # On affiche la confirmation de sauvegarde

    b2 = Bibliotheque()  # On cree une deuxième bibliotheque vide
    b2.charger_csv("livres.csv")  # On charge les donnees depuis le fichier CSV
    print("Donnees rechargees dans une nouvelle Bibliotheque")  # On affiche la confirmation

    b2.rendre("Ana", "1984")  # On teste le retour du livre par Ana
    print("Livre rendu avec succes par Ana dans la nouvelle bibliotheque !")  # On confirme la fin du test