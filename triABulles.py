import random

def tri_bulle(tableau):
    """Trie le tableau sur place avec le tri à bulles.

    Complexité : généralement O(n²), avec n le nombre d'éléments.
    Les éléments voisins sont comparés plusieurs fois, jusqu'à ce qu'il n'y
    ait plus aucun échange. Si le tableau est déjà trié, un seul passage est
    nécessaire : le tri est alors plus rapide, en O(n).
    """
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        passage = passage + 1
        for en_cours in range(0, len(tableau) - passage):
            if tableau[en_cours] > tableau[en_cours + 1]:
                permutation = True
                # On echange les deux elements
                tableau[en_cours], tableau[en_cours + 1] = tableau[en_cours + 1],tableau[en_cours]
    return tableau 

tab = [random.randint(0,20) for i in range(10)]
print(tab)
tri_bulle(tab)
print(tab)
