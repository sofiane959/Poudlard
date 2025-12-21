from utils.input_utils import demander_texte, demander_nombre, demander_choix, load_fichier
from univers.personnage import initialiser_personnage, afficher_personnage, modifier_argent, ajouter_objet

def introduction():
    print("\n" + "*"*50)
    print("⚡️BIENVENUE DANS LE MONDE DES SORCIERS ⚡️")
    print("*"*50)
    input("Appuyez sur Entrée pour commencer votre aventure...")

def creer_personnage() :
    print("\n--- CRÉATION DU PERSONNAGE ---")
    nom = demander_texte("Entrez le nom du personnage : ")
    prenom = demander_texte("Entrez le prenom du personnage : ")

    print("Répartissez vos attributs (1 à 10) :")
    attributs = {
        "courage": demander_nombre("Niveau de courage (1-10) : ", 1, 10),
        "intelligence": demander_nombre("Niveau de intelligence (1-10) : ", 1, 10),
        "loyauté": demander_nombre("Niveau de loyauté (1-10) : ", 1, 10),
        "ambition": demander_nombre("Niveau d'ambition (1-10) : ", 1, 10),
    }

    joueur = initialiser_personnage(nom, prenom, attributs)
    afficher_personnage(joueur)
    return joueur

def recevoir_lettre():
    print("\n🦉 Une chouette dépose une lettre devant vous. ")
    print("C'est une lettre de Poudlard !")
    choix = demander_choix("Voulez-vous ouvrir la lettre ?", ["Oui, bien sûr !", "Non je refuse. "])

    if choix == "Non je refuse. ":
        print("Vous déchirez la lettre. Vous resterez un Moldu pour toujours. Fin du jeu. ")
        exit()
    else:
        print("Vous lisez la lettre avec émerveillement. Vous êtes admis à Poudlard !")

def rencontrer_hagrid(joueur):
    print("\n🏠 Quelqu'un frappe à la porte... BOOM ! C'est Hagrid !")
    print(f"Hagrid: 'Salut {joueur['Prenom']} ! Tu es un sorcier. '")
    choix = demander_choix("Voulez vous suivre Hagrid au Chemin des Traverse ?", ["Oui", "Non"])
    if choix == "Non":
        print("Hagrid insiste et vous emmène de force (gentiment) !")

def acheter_fournitures(joueur):
    print("\n🏙️ BIENVENUE SUR LE CHEMIN DE TRAVERSE")
    catalogue = load_fichier("data/inventaire.json")

    if not catalogue:
        return

    obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]

    while True:
        print(f"\n💰 Votre bourse : {joueur['Argent']} galions")

        manquants = [obj for obj in obligatoires if obj not in joueur['Inventaire']]
        if not manquants:
            print("✅ Vous avez tous les objets obligatoires !")
            break

        print(f"⚠️ Il vous faut absolument : {','.join(manquants)}")

        options_menu = []
        ids_menu = []

        for k, v in catalogue.items():
            nom_objet = v[0]
            prix = v[1]
            options_menu.append(f"{nom_objet} ({prix} galions)")
            ids_menu.append(k)

        choix_str = demander_choix("Que voulez-vous acheter ?", options_menu)

        index = options_menu.index(choix_str)
        id_obj = ids_menu[index]
        nom_objet = catalogue[id_obj][0]
        prix = catalogue[id_obj][1]

        if prix > joueur['Argent']:
            print("❌ Vous n'avez pas assez d'argent !")
            if nom_objet in manquants:
                print("Game Over : Impossible d'acheter les fournitures scolaires. ")
                exit()
        else:
            modifier_argent(joueur, -prix)
            ajouter_objet(joueur, "Inventaire", nom_objet)
            print(f"🛒 Vous achetez : {nom_objet}")

    for obj in obligatoires:
        if obj not in joueur['Inventaire']:
            print("Vous avez oublié un objet obligatoire ! Perdu.")
            exit()

    print("\n🐾 Il vous reste un peu d'argent pour un animal. ")
    animaux = ["Chouette (20)", "Chat (15)", "Rat (10)", "Crapaud (5)"]
    choix_animal = demander_choix("Quel animal choisissez-vous ?", animaux)

    prix_animal = int(choix_animal.split('(')[1].replace(')', ''))
    nom_animal_seul = choix_animal.split('(')[0].strip()

    if prix_animal <= joueur['Argent']:
        modifier_argent(joueur, -prix_animal)
        ajouter_objet(joueur, "Inventaire", nom_animal_seul)
        print(f"Vous avez un nouveau compagnon : {nom_animal_seul} !")
    else:
        print("Dommage, pas assez d'argent pour l'animal.")

    afficher_personnage(joueur)

def lancer_chapitre_1():
    introduction()
    joueur = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(joueur)
    acheter_fournitures(joueur)
    print("\n🎬 Fin du Chapitre 1 ! En route pour Poudlard... ")
    return joueur