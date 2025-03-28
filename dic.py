def ajoute_dictionnaire(d1, d2):
    d = {}
    for i in d1:
        if i in d2:
            d[i] = d1[i] + d2[i]
        else:
            d[i] = d1[i]
    for i in d2:
        if i not in d:
            d[i] = d2[i]
    return d
d1 = {1: 5, 2: 7}
d2 = {}
print(ajoute_dictionnaire(d1, d2))
