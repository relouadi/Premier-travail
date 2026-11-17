"""Implémentation des files à l'aide de listes Python."""

class File:
    def __init__(self):
        self.data = []

    def est_vide(self):
        return not self.data

    def premier(self):
        return self.data[0]

    def enfiler(self, x):
        self.data.append(x)

    def defiler(self):
        if not self.data:
            raise IndexError("file vide")
        res = self.data[0]
        self.data.pop(0)  # Conservé comme dans le TAD fourni.
        return res

    def longueur(self):
        return len(self.data)

    def afficher(self):
        if self.est_vide():
            print("File vide")
        else:
            for i, elt in enumerate(self.data):
                print(i, ":", elt)
