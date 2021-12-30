import itertools


def powerset(l):
    pset = list()
    for n in range(len(l) + 1):
        for sset in itertools.combinations(l, n):
            pset.append(list(sset))
    return pset


def subsets_of_cardinality(L, c):
    ps = powerset(L)
    res = []
    for s in ps:
        if len(s) == c:
            res.append(s)
    return res
