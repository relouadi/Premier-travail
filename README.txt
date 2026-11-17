COMPTE EST BON — VERSION CORRIGÉE AU PLUS PRÈS DU CODE FOURNI

Fichiers :
- compteestbon.py : lecture des cartons et de la cible, puis lancement des trois parcours.
- recherche_compte_est_bon.py : parcours_DFS, parcours_DFS_recursif et parcours_BFS instrumentés.
- TAD/piles_listes_python.py : TAD Pile fourni, conservé.
- TAD/files_listes_python.py : TAD File fourni, conservé avec pop(0).
- TAD/notation_polonaise_inverse.py : évaluation NPI fournie, règles de calcul conservées.

Lancement depuis ce dossier :
    echo 50 4 100 2 7 3 526 | python compteestbon.py

Corrections apportées, sans réécriture générale :
1. empiler/enfiler ne prennent qu'un seul argument : le nœud complet est donc placé dans un tuple.
2. liste.append(...) modifie la liste et renvoie None : on construit désormais une nouvelle expression avec liste + [element].
3. Dans le BFS, les ajouts se font dans f et non dans p.
4. Dans le DFS récursif, cible_atteinte est partagée avec nonlocal et la solution est copiée avant le retour.
5. Le nœud contient désormais trois éléments : expression, cartons restants, profondeur. La profondeur sert uniquement aux indicateurs.

Les noms des trois fonctions principales, les noms essentiels des variables, les boucles et leur organisation ont été conservés. Les valeurs de retour d’origine sont également conservées : DFS/BFS renvoient (nb_noeuds, expression), et le DFS récursif renvoie (meilleure_expression, nb_noeuds). Les indicateurs supplémentaires sont placés dans le dictionnaire commun indicateurs.
La file conserve volontairement pop(0), conformément à la demande. Cela rend toutefois le BFS très lent lorsque la file devient très grande.

Indicateurs :
- nb_noeuds : nombre de nœuds effectivement retirés de la pile/file ou visités par la fonction récursive, donc évalués.
- taille_max_structure : maximum de nœuds simultanément en attente dans la pile ou la file.
- hauteur_max : profondeur maximale atteinte dans l'arbre (racine à profondeur 0 ; les nœuds invalides générés sont comptés).
- largeur_max : maximum du nombre de nœuds générés à une même profondeur.
- temps_s : temps mesuré à l'intérieur de chaque fonction, avec time.perf_counter(). Il inclut l'évaluation et la gestion de la structure.

Pour le DFS récursif, la taille de la pile d'appels Python n'est pas mesurée par le TAD Pile : le champ indique donc explicitement qu'elle n'est pas mesurée directement.

IMPORTANT — LIMITES DES ESSAIS EFFECTIVEMENT EXÉCUTÉS
Les essais ont été lancés avec ces entrées :
- 50 4 100 2 7 3 526
- 7 7 8 9 9 50 667
- 2 10 10 25 50 75 214

Les mesures partielles réellement obtenues sont consignées dans resultats_partiels.md.
Les parcours sur l'essai impossible ont dépassé la limite d'exécution de 300 s dans cet environnement ; ils ne sont donc pas présentés comme terminés.
Le BFS sur le premier essai a également dépassé 300 s avec pop(0). Il n'a pas été remplacé par une simulation ni par deque.
Un test BFS réduit [1, 2] -> 3 a bien été exécuté pour vérifier le fonctionnement de la file et du parcours.
