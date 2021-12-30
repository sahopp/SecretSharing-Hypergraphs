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


def covers_n_vertices(hg, nr_verts):
    verts = []
    for he in hg:
        verts += he
    return len(set(verts)) == nr_verts


def hg_hash(hg):
    hash_val = 0
    for e in hg:
        e.sort()
        hash_val += (107885204*e[0] + 3835246*e[1] + 3149*e[2]) ** 2
    return hash_val
