from random import randint

def Menu() -> None:
    menu_tuple = (
        "0. Arrêter de jouer",
        "1. Jouer"
    )
    for menu_str in menu_tuple:
        print(menu_str)
    choix = input("Veuillez faire votre choix >> ")
    boucle = True
    while boucle:
        if not int(choix) in [0, 1]:
            print("Veuillez choisir entre ces deux options uniquement.")
        else:
            boucle = False
    return choix

def DemandeLettre() -> str:
    """
    Cette fonction demande une lettre à l'utilisateur.

    Retourne:
        lettre (type: str): la lettre entrée par l'utilisateur en majusucle
    """
    boucle = True  # variable booléenne afin de simplifier la gestion des erreurs
    while boucle:
        # la méthode .strip() permet de retirer tous les espaces au début et à la fin de l'entrée et .upper() permet de mettre la lettre en majuscule
        lettre = input("Veuillez entrer une lettre >> ").strip().upper()
        if lettre == "":
            print("Merci de bien vouloir entrer une valeur non nulle.")
        elif len(lettre) > 1:
            print("Merci de bien vouloir entrer une seule lettre.")
        # la fonction ord() permet de récupérer le numéro ASCII de la lettre en question, dans la table ASCII 65 = "A" et 90 = "Z"
        elif 65 <= ord(lettre) <= 90:
            boucle = False  # si la lettre est comprise entre A et Z, la boucle est arrêtée
        else:
            print(
                "Merci de bien vouloir entrer une lettre comprise entre A et Z incluses.")
    return lettre


def AfficheListe(L: list) -> None:
    """
    Cette fonction affiche le mot contenu dans la liste sur une ligne et séparé par des espaces

    Paramètres : 
        L (type: list): la liste qui contient le mot à afficher
    """
    print(" ".join(L))


def AfficheMot(m: str) -> None:
    print(" ".join(m))


def AfficheReste(e: int, f: int) -> None:
    print(
        f"Il vous reste {f-e} erreur{'s' if f-e != 1 else ''} possible{'s' if not f-e in [0, 1] else ''}.")


def CreeMot(m: str, L: list) -> str:
    mot_tiret = ["-"] * len(m)
    for i in range(len(m)):
        if m[i] in L:
            mot_tiret[i] = m[i]
    return "".join(mot_tiret)


def MajListe(l: str, L: list) -> list:
    if l in L:
        return L
    else:
        L.append(l)
        return L


def ChoisirMot():
    """
    Renvoie un mot en majuscules de la liste MotsPendus.txt
    """
    fichier= open('MotsPendus.txt','r')
    num = randint(1, 1919)
    i = 0
    while i < num :
        mot = fichier.readline()
        i = i + 1
    fichier.close()
    mot_v = mot[:len(mot)-1]
    return mot_v.upper()


def main():
    boucle = True
    while boucle:
        choix = Menu()
        if choix == "0":
            print("Merci d'avoir jouer.")
            boucle = False
        else:
            lettresProposees = []
            nbErreursMax = 8
            erreurs = 0
            motCherche = ChoisirMot()
            motActuel = CreeMot(motCherche, lettresProposees)

            print("Bienvenue dans le jeu du pendu !")

            while erreurs < nbErreursMax and "-" in motActuel:
                AfficheMot(motActuel)
                AfficheListe(lettresProposees)
                AfficheReste(erreurs, nbErreursMax)

                lettre = DemandeLettre()

                if lettre in lettresProposees:
                    print(
                        f"La lettre '{lettre}' a déjà été proposée, cela fait une erreur en plus. Essayez encore.")
                    erreurs += 1
                else:
                    lettresProposees = MajListe(lettre, lettresProposees)
                    if lettre in motCherche:
                        print(f"La lettre '{lettre}' est dans le mot ! Bien joué !")
                    else:
                        print(
                            f"Dommage... La lettre '{lettre}' n'est pas dans le mot !")
                        erreurs += 1
                    motActuel = CreeMot(motCherche, lettresProposees)
            if "-" not in motActuel:
                print(
                    f"Félicitations ! Vous avez gagnez avec {erreurs} erreur{'s' if not erreurs in [0, 1] else ''}.")
            else:
                print(f"Désolé, nous sommes arrivés à cours d'essais... Le mot était {motCherche}")


main()
