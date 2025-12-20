def initialiser_personnage(nom, prenom, attributs):
    joueur = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs": attributs
    }
    return joueur

def afficher_personnage(joueur):
    print("\nProfil du personnage:")
    for cle in joueur:
        valeur = joueur[cle]
        if cle == "Attributs":
            print(f"{cle} :")
            for attr_cle in valeur:
                print(f"  {attr_cle}: {valeur[attr_cle]}")
        elif cle == "Inventaire" or cle == "Sortilèges":
            print(f"{cle} : {', '.join(valeur)}")
        else:
            print(f"{cle} : {valeur}")

def modifier_argent(joueur, montant):
    joueur["Argent"] = joueur["Argent"] + montant

def ajouter_objet(joueur, cle, objet):
    if cle == "Inventaire" or cle == "Sortilèges":
        joueur[cle].append(objet)