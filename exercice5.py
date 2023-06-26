def tuple_trie(list_tup):
    #la fonction sorted() pour trier les tuples
    #key=lambda x: x[1]indique que nous voulons trier les tuples en fonction de leur deuxième élément.
    #reverse = True qui permet de trier dans ordre decroissant
    tup_trie = sorted(list_tup, key=lambda x: x[1], reverse=True)
    return tup_trie

print(tuple_trie([(1,2), (3,4), (5,6)]))