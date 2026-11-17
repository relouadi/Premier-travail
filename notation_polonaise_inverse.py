"""Évaluation d'une expression NPI fournie dans une liste Python."""

from TAD.piles_listes_python import Pile


def eval_NPI_liste(listeExpression, afficher=False):
    # (False, None) : expression invalide
    # (True, None) : expression valide mais incomplète
    # (True, entier) : expression valide et calculable
    pile = Pile()
    for nextO in listeExpression:
        match nextO:
            case '+':
                if pile.est_vide():
                    return (False, None)
                op1 = pile.depiler()
                if pile.est_vide():
                    return (False, None)
                op2 = pile.depiler()
                pile.empiler(op1 + op2)
                if afficher:
                    print(op1, '+', op2, '=', op1 + op2)
            case '-':
                if pile.est_vide():
                    return (False, None)
                op1 = pile.depiler()
                if pile.est_vide():
                    return (False, None)
                op2 = pile.depiler()
                if op2 - op1 < 1:
                    return (False, None)
                pile.empiler(op2 - op1)
                if afficher:
                    print(op2, '-', op1, '=', op2 - op1)
            case '/':
                if pile.est_vide():
                    return (False, None)
                op1 = pile.depiler()
                if op1 == 0:
                    return (False, None)
                if pile.est_vide():
                    return (False, None)
                op2 = pile.depiler()
                if op2 % op1 != 0:
                    return (False, None)
                pile.empiler(op2 // op1)
                if afficher:
                    print(op2, '/', op1, '=', op2 // op1)
            case '*':
                if pile.est_vide():
                    return (False, None)
                op1 = pile.depiler()
                if pile.est_vide():
                    return (False, None)
                op2 = pile.depiler()
                pile.empiler(op1 * op2)
                if afficher:
                    print(op2, '*', op1, '=', op2 * op1)
            case _:
                pile.empiler(nextO)
    if pile.longueur() == 1:
        return (True, pile.sommet())
    return (True, None)
