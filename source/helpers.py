import itertools
from random import sample


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


# Factory for hash functions which map k-uniform hypergraphs onto integers
# Invariant wrt. order of hyperedges and order of vertices in hyperedges
class HypergraphHashFunctionFactory:
    def __init__(self, k):
        self.k = k
        self.rand_vals = sample(range(1, 1000), k)

    def compute_hash(self, hg):
        hash_val = 0
        for e in hg:
            assert len(e) == self.k
            assert len(set(e)) == self.k
            e.sort()
            he_hash = 0
            for i in range(self.k):
                he_hash += (self.rand_vals[i] * e[i])
            hash_val += he_hash ** 2
        return hash_val
