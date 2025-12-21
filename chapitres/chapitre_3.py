import random
from utils.input_utils import load_fichier, demander_texte
from univers.personnage import ajouter_objet, afficher_personnage
from univers.maison import actualiser_points_maison, afficher_maison_gagnante

def apprendre_sorts(joueur, chemin_ficier="data/sorts.json"):
    print("\n📚 COURS DE MAGIE")
    tous_les_sorts = load_fichier(chemin_ficier)

    if not tous_les_sorts:
        return

    offensifs = [s for s in tous_les_sorts if s['type'] == 'Offensif']
    defensifs = [s for s in tous_les_sorts if s['type'] == 'Défensif']
    utilitaires = [s for s in tous_les_sorts if s['type'] == 'Utilitaire']

    sorts_appris = []
    sorts_appris.append(random.choice(offensifs))
    sorts_appris.append(random.choice(defensifs))
    random.shuffle(utilitaires)
    sorts_appris.extend(utilitaires[:3])

    for sort in sorts_appris:
        ajouter_objet(joueur, "Sortilèges", sort)
        print(f"✨ Vous appprenez : {sort['nom']} ({sort['type']}) - {sort['description']}")
        input("Appuyez sur Entrée...")

def quiz_magie(joueur, maisons, chemin_fichier="data/quiz_magie.json") :
    print("\n❓ QUIZ DE MAGIE")
    questions = load_fichier(chemin_fichier)

    if not questions:
        return

    score_quiz = 0
    questions_posees = []
    while len(questions_posees) < 4:
        q = random.choice(questions)
        if q not in questions_posees:
            questions_posees.append(q)

    for i, q in enumerate(questions_posees, 1) :
        print(f"\nQuestion {i}: {q['question']}")
        reponse = demander_texte("Votre réponse : ")

        if reponse.lower() == q['reponse'].lower():
            print("✅ Bonne réponse ! (+25 points)")
            score_quiz += 25
        else:
            print(f"❌ Mauvaise réponse. C'était : {q['reponse']}")

    print(f"\nRésultat du quiz : {score_quiz} points. ")
    actualiser_points_maison(maisons, joueur['Maison'], score_quiz)

def lancer_chapitre_3(joueur, maisons):
    apprendre_sorts(joueur)
    quiz_magie(joueur, maisons)
    afficher_maison_gagnante(maisons)
    afficher_personnage(joueur)
    print("\n🎬 Fin du Chapitre 3 !")