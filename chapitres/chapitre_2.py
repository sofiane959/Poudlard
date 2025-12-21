from utils.input_utils import demander_choix, load_fichier
from univers.maison import repartition_maison
from univers.personnage import afficher_personnage

def rencontrer_amis(joueur):
    print("\n🚂 DANS LE POUDLARD EXPRESS")

    print("Un garcon roux arrive. ")
    choix = demander_choix("Ron: 'Je peux m'asseoir ?'", ["Oui", "Non"])
    if choix == "Oui" :
        joueur['Attributs']['loyauté'] += 1
    else:
        joueur['Attributs']['ambition'] += 1

    print("Une fille entre.")
    choix = demander_choix("Hermione: 'As-tu lu l'Histoire de la Magie ?'", ["Oui", "Non"])
    if choix == "Oui" :
        joueur['Attributs']['intelligence'] += 1
    else:
        joueur['Attributs']['courage'] += 1

    print("Un garçon blond au teint pâle entre.")
    print("Drago: 'Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?'")
    choix_drago = demander_choix("Comment réagissez-vous ?",
                                 ["Je lui serre la main poliment",
                                  "Je l'ignore complètement",
                                  "Je lui réponds avec arrogance"])

    if choix_drago == "Je lui serre la main poliment":
        joueur['Attributs']['ambition'] += 1
    elif choix_drago == "Je l'ignore complètement":
        joueur['Attributs']['loyauté'] += 1
    elif choix_drago == "Je lui réponds avec arrogance":
        joueur['Attributs']['courage'] += 1

    print(f"Vos attributs ont évolué : {joueur['Attributs']}")

def mot_de_bienvenue():
    print("\n🏰 Vous arrivez à Poudlard. ")
    print("Dumbledore: 'Bienveue à tous pour une nouvelle année !'")
    input("Appuyez sur Entrée...")

def ceremonie_repartition(joueur):
    print("\n🎩 CÉRÉMONIE DE RÉPARTITION")

    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l'aide", "Je reste calme et j'observe"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]

    maison = repartition_maison(joueur, questions)
    joueur['Maison'] = maison
    print(f"\n🎉 Le Choixpeau crie : {maison.upper()} !!!")
    print(f"Tu rejoins les élèves de {maison} sous les acclamations !")

def installation_salle_commune(joueur):
    data_maisons = load_fichier("data/maisons.json")
    nom_maison = joueur['Maison']
    if data_maisons and nom_maison in data_maisons:
        infos = data_maisons[nom_maison]
        print(f"\n🏠 Salle commune de {joueur['Maison']} : {infos['emoji']}")
        print(infos['description'])
        print(infos['message_installation'])
        print(f"Couleurs : {', '.join(infos['couleurs'])}")
    else:
        print("Erreur données maison. ")

def lancer_chapitre_2(joueur):
    rencontrer_amis(joueur)
    mot_de_bienvenue()
    ceremonie_repartition(joueur)
    installation_salle_commune(joueur)
    afficher_personnage(joueur)
    print("\n🎬 Fin du Chapitre 2 ! Les cours commencent... ")
