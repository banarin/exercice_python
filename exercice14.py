def dico_pro(dico):
    dic_toto = {}
    total_price = 1
    for key, sous_dic in dico.items():
        for sous_key,value in sous_dic.items():
            total_price *= value
        dic_toto[key] = total_price
    return dic_toto
print(dico_pro({'parastamol' : {'quantites': 2,'prix_unitaire': 100}}))