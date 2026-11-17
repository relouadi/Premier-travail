"""Lance les trois parcours pour les six cartons et la cible lus sur stdin."""

from recherche_compte_est_bon import *
import sys


def lire_stdin():
    """Lit l'entrée standard en invitant l'utilisateur si nécessaire."""
    if sys.stdin.isatty():
        sys.stderr.write("Saisissez du texte (Ctrl+D pour terminer) :\n")
    return sys.stdin.read()


if __name__ == "__main__":
    cartons_nombre = lire_stdin()
    *cartons, nombre = map(int, cartons_nombre.split())
    print(f"Recherche de {nombre} avec {cartons}")

    for nom, fonction in [
        ("DFS", parcours_DFS),
        ("DFS récursif", parcours_DFS_recursif),
        ("BFS", parcours_BFS)
    ]:
        resultat = fonction(cartons, nombre)
        # On conserve l'ordre de retour initial de chaque fonction.
        if nom == "DFS récursif":
            expression, nb_noeuds = resultat
        else:
            nb_noeuds, expression = resultat
        print(f"\n{nom}")
        print(f"  Cible atteinte : {indicateurs['cible_atteinte']}")
        print(f"  Expression : {expression}")
        print(f"  Nœuds évalués : {nb_noeuds}")
        print(f"  Temps : {indicateurs['temps_s']:.6f} s")
        print(f"  Hauteur maximale : {indicateurs['hauteur_max']}")
        print(f"  Largeur maximale : {indicateurs['largeur_max']}")
        print(f"  Taille maximale de la structure : {indicateurs['taille_max_structure']}")
