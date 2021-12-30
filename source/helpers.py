import itertools


# returns the powerset of a given list
def powerset(lst):
    pset = list()
    for n in range(len(lst) + 1):
        for sset in itertools.combinations(lst, n):
            pset.append(list(sset))
    return pset


# returns all subsets of a certain size of a given list
def subsets_of_cardinality(lst, size):
    ps = powerset(lst)
    res = []
    for s in ps:
        if len(s) == size:
            res.append(s)
    return res


# checks whether a hypergraph covers nr_verts vertices
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
