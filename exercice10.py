def ocur_char(mot):
    liste = list(mot)
    dico = {}
    for i in liste:
        if liste.count(i):
            dico[i] = liste.count(i)
    return dico
print(ocur_char("irin"))