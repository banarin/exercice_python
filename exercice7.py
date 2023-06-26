def dico_unique(dict):
    liste = list(dict.values())
    new_liste = []
    for i in liste:
        if liste.count(i) == 1:
            new_liste.append(i)
    return new_liste

print(dico_unique({'a': 1, 'b': 2,'c': 1, 'd': 2}))