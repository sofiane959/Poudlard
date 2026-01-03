import random

from utils.input_utils import load_fichier
from univers.maison import actualiser_points_maison
from univers.personnage import afficher_personnage

def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    joueurs_finaux = []
    equipe = {
        'nom': maison,
        'score': 0,
        'a_marque': 0,
        'a_stoppe': 0,
        'attrape_vifdor':False,
        'joueurs':[]
    }

    liste_joueurs_base = equipe_data.get('joueurs')
    if est_joueur and joueur :
        nom_complet = joueur['Prenom'] + " " + joueur['Nom'] + " (Attrapeur)"
        joueurs_finaux.append(nom_complet)

        for j in liste_joueurs_base:
            if "Attrapeur" not in j:
                joueurs_finaux.append(j)

        equipe['joueurs'] = joueurs_finaux
    else:
        equipe['joueurs'] = liste_joueurs_base

    return equipe

def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):

    proba_but = random.randint(1, 10)

    if proba_but >= 6:
        if joueur_est_joueur:
            buteur = equipe_attaque['joueurs'][0]
        else:
            buteur = random.choice(equipe_attaque['joueurs'])

        equipe_attaque['score'] = equipe_attaque['score'] + 10
        equipe_attaque['a_marque'] = equipe_attaque['a_marque'] + 1

        print("⚽️ " +buteur + " marque un but pour " + equipe_attaque['nom'] + " ! (+10 points)")
    else:
        equipe_defense['a_stoppee'] = equipe_defense['a_stoppe'] + 1
        print("🛡️ " + equipe_defense['nom'] + " bloque l'attaque !")


def apparition_vifdor():

    chance = random.randint(1, 6)
    if chance == 6:
        return True
    else:
        return False

def attraper_vifdor(e1, e2):

    equipes = [e1, e2]
    gagnant = random.choice(equipes)

    gagnant['score'] = gagnant['score'] + 150
    gagnant['attrape_vifdor'] = True

    return gagnant

def afficher_score(e1, e2):
    print("\n--- Score Actuel ---")
    print(e1['nom'] + " : " + str(e1['score']) + " points")
    print(e2['nom'] + " : " + str(e2['score']) + " points")

def afficher_equipe(maison, equipe):
    print("\nÉquipe de " + maison + ":")
    for j in equipe['joueurs']:
        print("-" + j)

def match_quidditch(joueur, maisons):
    print("\n" + "="*40)
    print("🧹 MATCH DE QUIDDITCH 🧹")
    print("="*40)

    data_quidditch = load_fichier('data/equipes_quidditch.json')
    if not data_quidditch:
        return

    maison_joueur = joueur['Maison']

    adversaires_possibles = []
    for m in data_quidditch:
        if m != maison_joueur:
            adversaires_possibles.append(m)

    maison_adversaires = random.choice(adversaires_possibles)

    equipe_joueur = creer_equipe(maison_joueur, data_quidditch[maison_joueur], est_joueur=True, joueur=joueur)
    equipe_adverse = creer_equipe(maison_adversaires, data_quidditch[maison_adversaires], est_joueur=False)

    afficher_equipe(maison_joueur, equipe_joueur)
    afficher_equipe(maison_adversaires, equipe_adverse)

    print("\nVous jouez pour " + maison_joueur + " en tant qu'Attrapeur !")
    input("Appuyez sur Entrée pour le coup d'envoi...")

    match_termine = False
    tour = 0
    max_tours = 20

    while not match_termine and tour < max_tours:
        tour += 1
        print("\n📣 Tour" + str(tour))

        tentative_marque(equipe_joueur, equipe_adverse, joueur_est_joueur=True)
        tentative_marque(equipe_adverse, equipe_joueur, joueur_est_joueur=False)

        afficher_score(equipe_joueur, equipe_adverse)

        if apparition_vifdor():
            print("\n✨ LE VIF D'OR EST APERCU !")
            equipe_gagnante_vif = attraper_vifdor(equipe_joueur, equipe_adverse)
            print("🏆 " + equipe_gagnante_vif['nom'] + " attraper le Vif d'Or ! (+150 points)")

            break
        else:
            input("Appuyez sur Entrée pour continuer...")

    print("🏁 FIN DU MATCH !")
    afficher_score(equipe_joueur, equipe_adverse)

    maison_gagnante_match = ""
    point_bonus = 0

    if equipe_joueur['score'] > equipe_adverse['score']:
        print("🥇 VICTOIRE DE " + maison_joueur.upper() + " !")
        maison_gagnante_match = maison_joueur
        point_bonus = 500
    elif equipe_adverse['score'] > equipe_joueur['score']:
        print("🥈 Victoire de " + maison_adversaires + "...")
        maison_gagnante_match = maison_adversaires
        point_bonus = 500
    else:
        print("🤝 Match nul !")


    if maison_gagnante_match != "" :
        print("La maison " + maison_gagnante_match + " remporte 500 points pour la Coupe !")
        actualiser_points_maison(maisons, maison_gagnante_match, point_bonus)


def lancer_chapitre_4(joueur, maisons):
    print("\n" + "="*40)
    print("🧹 CHAPITRE 4 : LA GRANDE FINALE 🧹")
    print("="*40)

    match_quidditch(joueur, maisons)

    print("\n🎬 Fin du Chapitre 4 ! Quelle performance incroyable sur le terrain !")
    
    from univers.maison import afficher_maison_gagnante
    afficher_maison_gagnante(maisons)
    
    afficher_personnage(joueur)