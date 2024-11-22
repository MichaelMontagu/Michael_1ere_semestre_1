def max_et_indice(l):
    length = len(l)
    grand = l[0]
    index = 0
    for i in range(1, length):
        if l[i] > grand:
            grand = l[i]
            index = i
    return grand, index

assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert max_et_indice([-2]) == (-2, 0)
assert max_et_indice([-1, -1, 3, 3, 3]) == (3, 2)
assert max_et_indice([1, 1, 1, 1]) == (1, 0)
