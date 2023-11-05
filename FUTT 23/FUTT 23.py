import random

class Joueur:
    def __init__(self, nom, valeur, score):
        self.nom = nom
        self.valeur = valeur
        self.score = score

class Equipe:
    def __init__(self, argent):
        self.argent = argent
        self.effectif = []

    def acheter_joueur(self, joueur):
        if self.argent >= joueur.valeur:
            self.argent -= joueur.valeur
            self.effectif.append(joueur)
            print(f"Vous avez acheté {joueur.nom} pour {joueur.valeur} €.")
        else:
            print("Fonds insuffisants pour acheter ce joueur.")

    def vendre_joueur(self, joueur):
        if joueur in self.effectif:
            self.argent += joueur.valeur
            self.effectif.remove(joueur)
            print(f"Vous avez vendu {joueur.nom} pour {joueur.valeur} €.")
        else:
            print(f"{joueur.nom} ne fait pas partie de votre équipe.")

    def afficher_equipe(self):
        print("Votre équipe :")
        for joueur in self.effectif:
            print(f"{joueur.nom} - Valeur : {joueur.valeur} € - Score : {joueur.score}")

def generer_joueur():
    noms_joueurs = ["Messi", "Ronaldo", "Neymar", "Mbappe", "Haaland", "De Bruyne"]
    nom = random.choice(noms_joueurs)
    valeur = random.randint(80, 1000)
    score = random.randint(60, 95)
    return Joueur(nom, valeur, score)

def main():
    argent = 3000000
    equipe = Equipe(argent)

    while True:
        print(f"Argent disponible : {equipe.argent} €")
        action = input("1. Acheter un joueur\n2. Vendre un joueur\n3. Afficher l'équipe\n4. Quitter\nChoisissez une action : ")

        try:
            action = int(action)  # Essayez de convertir l'entrée en un entier
        except ValueError:
            print("Action non valide. Veuillez choisir une action valide.")
            continue  # Revenir à la boucle pour demander une nouvelle action

        if action == 1:
            joueur_aleatoire = generer_joueur()
            equipe.acheter_joueur(joueur_aleatoire)
        elif action == 2:
            if equipe.effectif:
                joueur_a_vendre = random.choice(equipe.effectif)
                equipe.vendre_joueur(joueur_a_vendre)
            else:
                print("Votre équipe est vide. Achetez d'abord des joueurs.")
        elif action == 3:
            equipe.afficher_equipe()
        elif action == 4:
            print("Merci d'avoir joué à FUTT23.")
            break
        else:
            print("Action non valide. Veuillez choisir une action valide.")
if __name__ == "__main__":
    main()