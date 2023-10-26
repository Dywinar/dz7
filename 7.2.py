liste_1 = [13,3,4,5,19, 13, 26]
filtred = tuple(filter((lambda x: x % 19 == 0 or x % 13 == 0),liste_1 ))
print(filtred)
