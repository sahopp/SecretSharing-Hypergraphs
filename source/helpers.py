import itertools


def powerset(lst):
    pset = list()
    for n in range(len(lst) + 1):
        for sset in itertools.combinations(lst, n):
            pset.append(list(sset))
    return pset


def subsets_of_cardinality(lst, c):
    ps = powerset(lst)
    res = []
    for s in ps:
        if len(s) == c:
            res.append(s)
    return res
