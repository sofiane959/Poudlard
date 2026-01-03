Projet Poudlard : L'Art de Coder comme un Sorcier


1. Présentation Générale

Titre du Projet : Projet Poudlard - Aventure Interactive Python
Description brève : Un jeu de rôle textuel où le joueur vit sa première année à Poudlard, de l'achat des fournitures à la finale de Quidditch. Le projet utilise une architecture modulaire et des données externes en JSON.
Contributeurs : Hamouda Yanis & El Jarrari Sofiane
Installation :
    1. Cloner le dépôt : git clone : https://github.com/sofiane959/Poudlard
    2. Configuration : Aucune bibliothèque tierce n'est requise. Le projet utilise uniquement les modules standards random et json . Utiliser Python 3.8+. 

Utilisation :
    Exécution : Lancez le jeu avec la commande python main.py à la racine du projet.
    Instructions : Interagissez avec le terminal en saisissant les numéros des choix proposés.

Fonctionnalités Principales :
    1. Création de personnage avec attributs (Courage, Intelligence, etc.) . 
    2. Boutique interactive au Chemin de Traverse avec gestion de budget . 
    3. Test de personnalité du Choixpeau magique (Calcul pondéré : Attributs x2 + Quiz x3) . 
    4. Apprentissage aléatoire de sorts (quota : 1 off, 1 def, 3 util) . 
    5. Match de Quidditch avec simulateur de score et Vif d'Or .  


2. Journal de Bord


  Semaine 1 : 
    1. Mise en place de chapitre_1.py et de la boutique.
        a. Problème : On ne comprenait pas pourquoi le budget du joueur ne baissait pas après un achat.
        b. Résolution : On modifiait une copie de la variable locale au lieu de la clé dans le dictionnaire “joueur“. 
    
  Semaine 2 : 
    1. Algorithme de répartition dans maison.py.
        a. Problème : Le programme plantait avec une erreur KeyError: 'Maisons'.
        b. Résolution : On avait écrit "Maisons" (avec un s) dans l'initialisation et "Maison" (sans s) dans le chapitre 2. 

  Semaine 3 :
    1. Système d'apprentissage des sorts et Quiz dans chapitre_3.py.
        a. Problème : On s'est rendu compte que le joueur pouvait apprendre trois fois le même sort utilitaire par "malchance", ce qui rendait l'inventaire inutile.
        b. Résolution : On a utiliser une boucle while combinée à la condition if sort not in liste_apprise pour forcer des tirages uniques.
         
  Semaine 4 :
    1. Moteur de match dans chapitre_4.py.
        a. Problème : Le match continuait jusqu'au tour 20 même si le Vif d'Or était attrapé.
        b. Résolution : On avait oublié de placer l'instruction break. En se relisant mieux on a trouvé l'erreur et ajouter break pour que l'effet attendu arrive.

  
  Tout au long du projet on a eu pas mal de difficulté avec Github ce qui rend notre travail tres peu comprehensible en suivant les commits 

  
Chronologie du Projet :

Répartition des Tâches :
  Yanis : Logique système (input_utils.py), algorithme de répartition, moteur de Quidditch et gestion JSON.
  Sofiane : Narration des chapitres, gestion du personnage, création des quiz et documentation.


  
3. Contrôle, Tests et Validation
  Gestion des Entrées et Erreurs :
           Validation : demander_nombre vérifie les entiers et les intervalles min/max .
          Prévention des Plantages : Utilisation de .strip() pour les espaces et .lower() pour les réponses aux quiz.
   Bugs connus : 
          Format des noms : Le programme accepte des chiffres dans les noms (ex: "Harry2"), car il n'y a pas de filtre spécifique sur les caractères spéciaux dans demander_texte.
          Doublons de sorts : Dans de rares cas d'aléatoire, si le fichier sorts.json était très court, le joueur pourrait apprendre deux fois le même sort car le filtre de doublons repose sur le hasard.
          Affichage : Les longs textes de descriptions peuvent parfois déformer les cadres de décoration (= ou *) selon la taille de la console de l'utilisateur.

  Stratégies de Test :
         Test de Budget : Achat de la Cape d'Invisibilité (100G). Résultat : Le système refuse tout achat suivant par manque de fonds.
         <img width="1512" height="982" alt="test_budget" src="https://github.com/user-attachments/assets/b213aa7d-162c-46fb-85fa-f74032d4a79f" />
          Test de Répartition : Saisie de réponses "Serpentard" avec ambition élevée. Résultat : La maison est validée par le calcul des coefficients.
          <img width="1512" height="982" alt="test_Répartition-1" src="https://github.com/user-attachments/assets/0d5ff039-ac96-4162-bf48-8c2dca6283f4" />
          <img width="1512" height="982" alt="test_Répartition-2" src="https://github.com/user-attachments/assets/f4d36cb3-d977-4ab2-9381-914d846ad65e" />
         Test de Quidditch : Capture du Vif d'Or au tour 5. Résultat : Le match s'arrête immédiatement avec +150 points pour l'équipe .
         <img width="1512" height="982" alt="test_Vif-D&#39;Or" src="https://github.com/user-attachments/assets/51888d92-09ba-472f-a168-fee1c6dbee1e" />

