import random

def tri_insertion(tableau):
    """Trie le tableau sur place avec le tri par insertion.

    Complexité : généralement O(n²), avec n le nombre d'éléments.
    Une valeur peut devoir être décalée devant beaucoup d'autres valeurs.
    Si le tableau est déjà trié, aucun décalage n'est nécessaire : le tri est
    alors plus rapide, en O(n).
    """
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        # décalage des éléments du tableau 
        while j>0 and tableau[j-1]>en_cours:
            tableau[j]=tableau[j-1]
            j = j-1
        # on insère l'élément à sa place
        tableau[j]=en_cours

tab = [random.randint(0,20) for i in range(10)]
print(tab)
tri_insertion(tab)
print(tab)
