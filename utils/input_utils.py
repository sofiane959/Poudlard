from operator import truediv


def demander_texte(message):
    while True:
        saisie = input(message)
        texte_nettoye = saisie.strip()

        if texte_nettoye:
            return texte_nettoye
        else:
            print("Erreur: La saisie ne peut pas etre vide.Veillez entrer du texte.")

def demander_nombre(message, min_val=None, max_val=None)
    while true:
        saisie = input(message).strip()

        if not saisie:
            print("Erreur: La saisie ne peut pas etre vide.")
            continue
        est_negatif = false
        chaine_chiffres = saisie
        if saisie[0]== '-':
            est_negatif = true
            chaine_chiffres = saisie[1:]

        est_valide = true
        if not chaine_chiffres:
            est_valide = false
        else:
            for char in chaine_chiffres:
                if not('0'<=char<='9'):
                    est_valide = false
                    break

        if not est_valide:
            print("Erreur:Saisie invalide. Veuillez entrer un nombre entier.")
            continue

        nombre = int(saisie)

        is_valid_range = true

        if min_val is not None and nombre < min_val:
            is_valid_range = False
        if max_val is not None and nombre > max_val:
            is_valid_range = False
        if is_valid_range:
            return nombre
        else:
            range_message = ""
            if min_val is not None and max_val is not None:
                range_message = f"entre {min_val} et {max_val}."
            elif min_val is not None:
                range_message = f"supèrieur ou égal à {min_val}."
            elif max_val is not None:
                range_message = f"inférieur ou égale a {max_val}."


def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")

    choix_index = demander_nombre("Votre choix : ", 1, len(options))
    return options[choix_index - 1]


def load_fichier(chemin_fichier):
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        donnees = json.load(f)
        return donnees

