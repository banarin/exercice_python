
file = open("file.txt", "r")
text = file.read()
liste = list(text.split(" "))
nbr_mot = len(liste)
file.close()
print(text)
print(liste)
print("le nombre de mots est " + str(nbr_mot))
