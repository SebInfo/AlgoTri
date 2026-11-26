import random 

def tri_selection(tableau):
    nb = len(tableau)
    for en_cours in range(0,nb-1):    
        plus_petit = en_cours
        for j in range(en_cours+1,nb) :
            if tableau[j] < tableau[plus_petit] :
                plus_petit = j
        if plus_petit is not en_cours :
            temp = tableau[en_cours]
            tableau[en_cours] = tableau[plus_petit]
            tableau[plus_petit] = temp

def plus_petit(tableau: list[int], debut: int = 0) -> int:
    if len(tableau) == 0:
        raise ValueError("Le tableau ne peut pas être vide.")

    if debut < 0 or debut >= len(tableau):
        raise ValueError("L'indice de départ doit appartenir au tableau.")

    indice_petit = debut
    for i in range(debut + 1, len(tableau)):
        if tableau[i] < tableau[indice_petit]:
            indice_petit = i          
    return indice_petit #on retourne ici l'indice


def tri_selection_avec_plus_petit(tableau):
    for en_cours in range(len(tableau) - 1):
        indice_plus_petit = plus_petit(tableau, en_cours)
        # On réalise une permutation 
        if indice_plus_petit != en_cours:
            tableau[en_cours], tableau[indice_plus_petit] = (
                tableau[indice_plus_petit],
                tableau[en_cours],
            )


tab = [random.randint(-90,90) for i in range(10)]
tab1 = [12]
print (plus_petit(tab1))
print(tab)
tri_selection(tab)
print(tab)
