"""Parcours de l'arbre de calculs à la volée : DFS, DFS récursif et BFS."""

from TAD.notation_polonaise_inverse import *
from TAD.piles_listes_python import *
from TAD.files_listes_python import *
import time

# Dictionnaire commun : les fonctions conservent leurs valeurs de retour initiales.
indicateurs = {}


def parcours_DFS(cartons, cible):
    # cartons : une liste ; cible : entier
    debut = time.perf_counter()
    nb_noeuds = 0
    p = Pile()
    operateurs = ['+', '-', '*', '/']
    p.empiler(([], cartons[:], 0))  # racine : expression, cartons restants, profondeur
    taille_max_pile = 1
    largeur_niveaux = {0: 1}
    while p.est_vide() == False:
        noeud = p.depiler()
        nb_noeuds += 1
        valide, resultat = eval_NPI_liste(noeud[0])
        if valide:
            if resultat == cible:
                fin = time.perf_counter()
                indicateurs.clear()
                indicateurs.update({
                    "nb_noeuds": nb_noeuds,
                    "taille_max_structure": taille_max_pile,
                    "hauteur_max": max(largeur_niveaux),
                    "largeur_max": max(largeur_niveaux.values()),
                    "temps_s": fin - debut,
                    "largeur_niveaux": largeur_niveaux,
                    "cible_atteinte": True
                })
                return nb_noeuds, noeud[0]
            nb_enfants = 0
            for i in range(len(noeud[1])):
                nouvelle_expression = noeud[0] + [noeud[1][i]]
                p.empiler((nouvelle_expression,
                           noeud[1][:i] + noeud[1][i+1:], noeud[2] + 1))
                nb_enfants += 1
            for i in range(len(operateurs)):
                nouvelle_expression = noeud[0] + [operateurs[i]]
                p.empiler((nouvelle_expression, noeud[1][:], noeud[2] + 1))
                nb_enfants += 1
            largeur_niveaux[noeud[2] + 1] = largeur_niveaux.get(noeud[2] + 1, 0) + nb_enfants
            if p.longueur() > taille_max_pile:
                taille_max_pile = p.longueur()
    fin = time.perf_counter()
    indicateurs.clear()
    indicateurs.update({
        "nb_noeuds": nb_noeuds,
        "taille_max_structure": taille_max_pile,
        "hauteur_max": max(largeur_niveaux),
        "largeur_max": max(largeur_niveaux.values()),
        "temps_s": fin - debut,
        "largeur_niveaux": largeur_niveaux,
        "cible_atteinte": False
    })
    return nb_noeuds, "Cible non atteinte"


def parcours_BFS(cartons, cible):
    # cartons : une liste ; cible : entier
    debut = time.perf_counter()
    nb_noeuds = 0
    f = File()
    operateurs = ['+', '-', '*', '/']
    f.enfiler(([], cartons[:], 0))  # racine : expression, cartons restants, profondeur
    taille_max_file = 1
    largeur_niveaux = {0: 1}
    while f.est_vide() == False:
        noeud = f.defiler()
        nb_noeuds += 1
        valide, resultat = eval_NPI_liste(noeud[0])
        if valide:
            if resultat == cible:
                fin = time.perf_counter()
                indicateurs.clear()
                indicateurs.update({
                    "nb_noeuds": nb_noeuds,
                    "taille_max_structure": taille_max_file,
                    "hauteur_max": max(largeur_niveaux),
                    "largeur_max": max(largeur_niveaux.values()),
                    "temps_s": fin - debut,
                    "largeur_niveaux": largeur_niveaux,
                    "cible_atteinte": True
                })
                return nb_noeuds, noeud[0]
            nb_enfants = 0
            for i in range(len(noeud[1])):
                nouvelle_expression = noeud[0] + [noeud[1][i]]
                f.enfiler((nouvelle_expression,
                           noeud[1][:i] + noeud[1][i+1:], noeud[2] + 1))
                nb_enfants += 1
            for i in range(len(operateurs)):
                nouvelle_expression = noeud[0] + [operateurs[i]]
                f.enfiler((nouvelle_expression, noeud[1][:], noeud[2] + 1))
                nb_enfants += 1
            largeur_niveaux[noeud[2] + 1] = largeur_niveaux.get(noeud[2] + 1, 0) + nb_enfants
            if f.longueur() > taille_max_file:
                taille_max_file = f.longueur()
    fin = time.perf_counter()
    indicateurs.clear()
    indicateurs.update({
        "nb_noeuds": nb_noeuds,
        "taille_max_structure": taille_max_file,
        "hauteur_max": max(largeur_niveaux),
        "largeur_max": max(largeur_niveaux.values()),
        "temps_s": fin - debut,
        "largeur_niveaux": largeur_niveaux,
        "cible_atteinte": False
    })
    return nb_noeuds, "Cible non atteinte"


def parcours_DFS_recursif(cartons, cible):
    debut = time.perf_counter()
    nb_noeuds = 0
    meilleure_expression = []
    operateurs = ['+', '-', '*', '/']
    cible_atteinte = False
    largeur_niveaux = {0: 1}
    hauteur_max = 0

    def parcours_DFSR_aux(choisis, restants, profondeur):
        nonlocal nb_noeuds, meilleure_expression, cible_atteinte
        nonlocal hauteur_max
        nb_noeuds += 1
        hauteur_max = max(hauteur_max, profondeur)
        valide, resultat = eval_NPI_liste(choisis)
        if not valide:
            return
        if resultat == cible:
            meilleure_expression = choisis[:]
            cible_atteinte = True
            return
        nb_enfants = 0
        for i in range(len(restants)):
            if not cible_atteinte:
                nb_enfants += 1
                parcours_DFSR_aux(
                    choisis + [restants[i]],
                    restants[:i] + restants[i+1:],
                    profondeur + 1)
        for operateur in operateurs:
            if not cible_atteinte:
                nb_enfants += 1
                parcours_DFSR_aux(
                    choisis + [operateur],
                    restants[:],
                    profondeur + 1)
        largeur_niveaux[profondeur + 1] = largeur_niveaux.get(profondeur + 1, 0) + nb_enfants

    parcours_DFSR_aux([], cartons[:], 0)
    fin = time.perf_counter()
    indicateurs.clear()
    indicateurs.update({
        "nb_noeuds": nb_noeuds,
        "taille_max_structure": "non mesurable directement (pile d'appels)",
        "hauteur_max": hauteur_max,
        "largeur_max": max(largeur_niveaux.values()),
        "temps_s": fin - debut,
        "largeur_niveaux": largeur_niveaux,
        "cible_atteinte": cible_atteinte
    })
    return meilleure_expression if cible_atteinte else "Cible non atteinte", nb_noeuds
