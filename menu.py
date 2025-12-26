from utils.input_utils import demander_texte
from chapitres.chapitre_1 import lancer_chapitre_1
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_3 import lancer_chapitre_3
from chapitres.chapitre_4 import lancer_chapitre_4



def afficher_menu_principal():
    print("\n" + "="*40)
    print("🏰 MENU PRINCIPAL POUDELARD")
    print("="*40)
    print("1. Lancer l'aventure (Chapitres 1 à 4)")
    print("2. Quitter le jeu")
    print("="*40)


def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    while True:
        afficher_menu_principal()
        choix = demander_texte("Votre choix : ")

        if choix == "1":
            print("\n🚀 Lancement de l'aventure...")

            joueur = lancer_chapitre_1()

            input("\n✨ Appuyez sur Entrée pour voyager vers Poudlard (Chapitre 2)...")
            lancer_chapitre_2(joueur)

            input("\n✨ Appuyez sur Entrée pour commencer les cours (Chapitre 3)...")
            lancer_chapitre_3(joueur, maisons)

            input("\n🧹 Appuyez sur Entrée pour commencer le Grand Match de Quidditch (Chapitre 4)... ")
            lancer_chapitre_4(joueur, maisons)

            print("\n🏆 Félicitations ! Vous avez terminé l'aventure.")
            print("Merci d'avoir joué au Projet Poudelard.")

        elif choix == "2":
            print("Au revoir et a bientôt dans le monde des sorciers !")
            break
        else:
            print("❌ Choix invalide. Veuillez entrer 1 ou 2.")