class Livre:
    def __init__(self,titre,auteur,annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True #On définit par défaut la disponibilité du livre à "true"(vrai)
        self.emprunteur = None #On définit par défaut que livre n'est pas emprunté

    def afficher(self):
        print(self.titre, "par" ,self.auteur ,"l'annee est : ", self.annee) # On affiche les informations du livre

    def emprunter(self,nom):
        if self.disponible == True: #On vérifie si le livre est libre
            self.disponible = False
            self.emprunteur = nom # ON attribue le nom à l'emprunteur du livre
            return True
        else:
            print("Ce livre n'est pas disponible") # Si le livre est deja pris, l'emprunt echoue
            return False
    def rendre(self):
        if self.disponible == False:
            self.disponible = True 
            self.emprunteur = None
            return True
        else:
            return False
class Utilisateur:
    def __init__(self,nom):
        self.nom = nom
        self.emprunts = [] #Création d'une liste vide pour stocker les objets Livre empruntés.        
    def emprunter_livre(self, livre):
        if livre.emprunter(self.nom) == True: # On tente d'emprunter le livre et l'ajoute a la liste si le resultat est True
            self.emprunts.append(livre)  #Ajout du livre grâce à append dans la liste self.emprunts
    def rendre_livre(self, livre): # ON retire le livre de la liste des emprunts s'il y figure et le rend
        if livre in self.emprunts:
            livre.rendre()
            self.emprunts.remove(livre) #Suppression du livre dans la liste avec le remove
    def afficher_emprunts(self):  
        for livre in self.emprunts:   # Parcourt la liste des livres empruntes
            print(self.titre) #Affichage des livres empruntés
#Jeu d'essai
l = Livre("1984", "Orwell",1949)
l = Livre("Blard","Samuel",)
print(l.emprunter("Ana")) #Affichage du livre emprunté par Ana en appellant la méthode emprunter
print(l.emprunter("Léo")) #Affichage du livre emprunté par Léo en appellant la méthode emprunter
print(l.rendre())  #Appel de la méthode rendre et affichage du résultat
l.afficher()