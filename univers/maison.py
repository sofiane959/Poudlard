def actualiser_points_maison(maisons, nom_maison, points):
    if nom_maison in maisons:
        maisons[nom_maison] = maisons[nom_maison] + points
        print(f"{nom_maison} : {points} points. Nouveau total : {maisons[nom_maison]}")
    else:
        print("Erreur : Maison introuvable.")


def afficher_maison_gagnante(maisons):
    score_max = -1
    for nom in maisons:
        if maisons[nom] > score_max:
            score_max = maisons[nom]

    gagnantes = []
    for nom in maisons:
        if maisons[nom] == score_max:
            gagnantes.append(nom)

    if len(gagnantes) == 1:
        print(f"La maison gagnante est {gagnantes[0]} avec {score_max} points !")
    else:
        noms_ex_aequo = ", ".join(gagnantes)
        print(f"Les maisons ex æquo sont : {noms_ex_aequo} avec {score_max} points !")


def repartition_maison(joueur, questions):
    scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    attr = joueur["Attributs"]
    scores["Gryffondor"] = attr["courage"] * 2
    scores["Serpentard"] = attr["ambition"] * 2
    scores["Poufsouffle"] = attr["loyauté"] * 2
    scores["Serdaigle"] = attr["intelligence"] * 2

    from utils.input_utils import demander_choix

    for q_texte, q_options, q_maisons in questions:
        reponse = demander_choix(q_texte, q_options)

        index_maison = -1
        for i in range(len(q_options)):
            if q_options[i] == reponse:
                index_maison = i
                break

        maison_choisie = q_maisons[index_maison]
        scores[maison_choisie] = scores[maison_choisie] + 3

    maison_finale = ""
    max_pts = -1
    for m in scores:
        if scores[m] > max_pts:
            max_pts = scores[m]
            maison_finale = m

    return maison_finale