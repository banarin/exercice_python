def fusion_dic(dic1, dic2):

    dico_fus = dic1.copy()
    
    for cle,value in dic2.items():
        if cle in dico_fus.keys():
            dico_fus[cle] += value
        else:
            dico_fus[cle] = value
    return dico_fus
print(fusion_dic({'a': 1, 'b': 2, 'c': 3},{'a': 1, 'b': 2, 'c': 3}))