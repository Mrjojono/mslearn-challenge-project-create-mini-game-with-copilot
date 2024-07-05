import random
liste_choix = ["rock","paper","sciccors"]
dic_jeu = {}
def choix_joueur():
    while True:
        choix = input("quel est votre choix: ")
        if choix  in liste_choix:
            return choix
        else:
             print("mauvais choix,veuillez retaper\n ")
        
def choix_ordinateur():
    return random.choice(liste_choix)

print("Début du jeu\n")
print("====================================\n")
print("Entrez votre nom: ")
print("====================================\n")
nom = input()

while True:
    print(f"Voici les choix possibles: {(liste_choix)}")
    dic_jeu[nom] = choix_joueur()
    dic_jeu["ordinateur"] = choix_ordinateur()
    if dic_jeu[nom] == dic_jeu["ordinateur"]:
        print("Egalité")
    elif dic_jeu[nom] == "rock" and dic_jeu["ordinateur"] == "sciccors":
        print("Vous avez gagné")
    elif dic_jeu[nom] == "paper" and dic_jeu["ordinateur"] == "rock":
        print("Vous avez gagné")
    elif dic_jeu[nom] == "sciccors" and dic_jeu["ordinateur"] == "paper":
        print("Vous avez gagné")
    elif dic_jeu["ordinateur"] == "rock" and dic_jeu[nom] == "sciccors":
        print("Vous avez perdu")
    elif dic_jeu["ordinateur"] == "paper" and dic_jeu[nom] == "rock":
        print("Vous avez perdu")
    elif dic_jeu["ordinateur"] == "sciccors" and dic_jeu[nom] == "paper":
        print("Vous avez perdu")
    print("Voulez-vous jouer? oui/non")
    if input() == "non":
        break




            