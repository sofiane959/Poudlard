import json


def demander_texte(message):
    while True:
        texte = input(message).strip()
        if texte:
            return texte
        print("Erreur: La saisie ne peut pas etre vide. ")


def demander_nombre(message, min_val=None, max_val=None):
    while True:
        saisie = input(message).strip()

        if (saisie.isdigit()) or (saisie.startswith('-') and saisie[1:].isdigit()):
            valeur = int(saisie)
            if (min_val is not None and valeur < min_val) or (max_val is not None and valeur > max_val):
                print(f"Veuillez entrer un nombre entre {min_val} et {max_val}")
            else:
                return valeur

        else:
            print("Erreur: Veuillez entrer un nombre valide. ")


def demander_choix(message, options):
    print(message)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choix = demander_nombre("Votre choix : ", 1, len(options))
    return options[choix - 1]


def load_fichier(chemin_fichier):
    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            donnees = json.load(f)
        return donnees
    except FileNotFoundError:
        print(f"Erreur : le fichier {chemin_fichier} est introuvable.")
        return []
