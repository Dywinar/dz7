liste_1 = [1,3,4,5,4]
liste_2 = [4]
while len(liste_1) != len(liste_2):
  if len(liste_1) >= len(liste_2):
    liste_2.append(0)
  else:
    liste_1.append(0)
summ = list(map(lambda x, y: x + y,liste_1 , liste_2)) 
print(summ)
