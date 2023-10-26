from functools import reduce
liste_1 = [13,3,4,5,19, 13, 26]
reduce_max = reduce((lambda x, y: x if x>= y else y), liste_1)
print(reduce_max)
