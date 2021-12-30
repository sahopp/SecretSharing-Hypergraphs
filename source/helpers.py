import itertools


def powerset(l):
    pset = list()
    for n in range(len(l) + 1):
        for sset in itertools.combinations(l, n):
            pset.append(list(sset))
    return pset