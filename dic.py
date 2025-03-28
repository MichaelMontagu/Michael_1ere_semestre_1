def ajoute_dictionnaire(d1, d2):
    minval = 0
    d = {}
    l1 = d1.keys()
    l2 = d1.values()
    l3 = d2.keys()
    l4 = d2.values()
    length_1 = len(l1)
    length_2 = len(l2)
    if length_1 < length_2:
        minval = length_1
    else:
        minval = length_2

    for i in range(minval - 1):
        if l1[i] == l3[i]:
            d[l1[i] = l2[i]]

d1 = {1: 5, 2: 7,}
d2 = {2: 9, 3: 11}