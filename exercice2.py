def fichier(name):
    file = open( name +".txt", "r")
    text = file.read()
    count = 0
    for i in text:
        if i.strip() == '':
            count += 1
    return  count
print('le nombre de ligne vide est : ' + str(fichier('file')))
