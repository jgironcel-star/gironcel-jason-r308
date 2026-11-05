from PartieA import Livre, Utilisateur  # Import des classes créées dans la Partie A

class Bibliotheque:
    def __init__(self):
        self.livres = {} # on créer un dictionnaire vide pour stocker les livres
        self.utilisateurs = {} # on créer un dictionnaire vide pour stocker les utilisateurs

    def ajouter_livre(self, livre):
        self.livres[livre.titre] = livre # On associe le titre du livre à son objet Livre

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs[utilisateur.nom] = utilisateur  # On associe le nom de l'utilisateur à son objet Utilisateur

    def emprunter(self, nom, titre):
        # On verifie que l'utilisateur ET le livre existent bien dans les dictionnaires
        if nom in self.utilisateurs and titre in self.livres:
            u = self.utilisateurs[nom] #On Recupere l'objet utilisateur correspondant au nom
            l = self.livres[titre] #On Recupere l'objet livre correspondant au titre
            u.emprunter_livre(l) # Appel de la methode emprunter_livre faite dans la partie A sur l'objet utilisateur
        else: #  Si le nom ou le titre n'exstent pas , on affichage d'un message 
            print("Erreur : Nom ou titre inconnu.")

    def rendre(self, nom, titre):
        if nom in self.utilisateurs and titre in self.livres:  # Verification que l'utilisateur ET le livre existent
            u = self.utilisateurs[nom]  #On récupére l'objet nom
            l = self.livres[titre] #On récupérer l'objet livre
            u.rendre_livre(l) # Appel de la methode pour rendre le livre
        else: 
            print("Erreur : Nom ou titre inconnu.")

    def afficher_livres(self):
        print("Livres disponibles")
        for livre in self.livres.values(): #boucle permettant de parcourir chaque livre du dictionnaire
            if livre.disponible == True:  # On teste si le livre est marque comme disponible 
                livre.afficher()

        print("Livres empruntes")
        for livre in self.livres.values(): #boucle permettant de parcourir chaque livre du dictionnaire
            if livre.disponible == False: # On teste si le livre est marque comme emprunte
                print(livre.titre, "par", livre.auteur, "- emprunte par", livre.emprunteur)
#Jeu d'essai de la Partie B
if __name__ == "__main__": # On verifie si le fichier est execute directement
    b = Bibliotheque()
    # Creation des livres et utilisateurs
    l1 = Livre("1984", "Orwell", 1949)
    l2 = Livre("Dune", "Herbert", 1965)
    u1 = Utilisateur("Ana")
    u2 = Utilisateur("Léo")

    # Ajout à la bibliothèque
    b.ajouter_livre(l1)
    b.ajouter_livre(l2)
    b.ajouter_utilisateur(u1)
    b.ajouter_utilisateur(u2)

    # Tests d'emprunts et d'erreurs
    b.emprunter("Ana", "1984")
    b.emprunter("Léo", "1984")       # Livre déjà emprunté -> échec sans plantage
    b.emprunter("Inconnu", "1984")   # Nom inconnu -> échec sans plantage
    b.emprunter("Ana", "Inconnu")    # Titre inconnu -> échec sans plantage

    b.afficher_livres()    # Affichage de l'état            