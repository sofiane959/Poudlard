ef
afficher_menu_principal():
print("AVENTURE A POUDELARD")
print("1. Nouvelle Partie")
print("2. Quitter le jeu")


def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    continuer = True
    while continuer:
        afficher_menu_principal()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            # On importe les chapitres seulement quand on lance la partie
            from chapitres.chapitre_1 import lancer_chapitre_1
            from chapitres.chapitre_2 import lancer_chapitre_2
            from chapitres.chapitre_3 import lancer_chapitre_3

            # Enchaînement automatique des chapitres
            personnage = lancer_chapitre_1()
            if personnage:
                lancer_chapitre_2(personnage)
                lancer_chapitre_3(personnage, maisons)

        elif choix == "2":
            print("Au revoir !")
            continuer = False
        else:
            print("Choix invalide.")