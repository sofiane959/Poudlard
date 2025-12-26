def initialiser_personnage(nom, prenom, attributs):
    joueur = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs": attributs,
        "Maison" : None
    }
    return joueur

def afficher_personnage(joueur):
    print("\nProfil du personnage:")
    for cle in joueur:
        liste_noms = []
        valeur = joueur[cle]
        if cle == "Attributs":
            print(f"{cle} :")
            for attr_cle in valeur:
                print(f"  {attr_cle}: {valeur[attr_cle]}")
        elif cle == "Inventaire" or cle == "Sortilèges":
            for item in valeur:
                if isinstance(item, dict):
                    liste_noms.append(item['nom'])
                else:
                    liste_noms.append(str(item))

        print(f"{cle} : {', '.join(liste_noms)}")
def modifier_argent(joueur, montant):
    joueur["Argent"] = joueur["Argent"] + montant

def ajouter_objet(joueur, cle, objet):
    if cle == "Inventaire" or cle == "Sortilèges":
        joueur[cle].append(objet)