from HypergraphFactory import *


class CompleteMultipartiteFactory(HypergraphFactory):
    def __init__(self, k, v_set):
        self.k = k
        self.v_set = v_set

    @staticmethod
    def powerset(l):
        pset = list()
        for n in range(len(l) + 1):
            for sset in itertools.combinations(l, n):
                pset.append(list(sset))
        return pset

    def subsets_of_cardinality(self, L, c):
        ps = self.powerset(L)
        res = []
        for s in ps:
            if len(s) == c:
                res.append(s)
        return res

    def create_complete_multipartite_k_hg(self, partition):
        i = 0
        parts = []
        for p in partition:
            parts.append(self.v_set[i:i + p])
            i += p
        he = []
        combs = self.subsets_of_cardinality(parts, self.k)
        for comb in combs:
            he += self.all_k_combs(comb)
        return he

    def all_k_combs(self, partition):
        res = []
        if len(partition) == 1:
            for i in partition[0]:
                res.append([i])
        else:
            rec_part = self.all_k_combs(partition[1:])
            for i in partition[0]:
                for j in rec_part:
                    res.append([i] + j)
        return res

    def get_complete_multipartite_k_hgs(self):
        all_cm_hgs = []
        part_numbers = self.partition_sizes(len(self.v_set), 1, self.k)
        for partition in part_numbers:
            all_cm_hgs.append(self.create_complete_multipartite_k_hg(partition))
        return all_cm_hgs

    def get_hypergraphs(self):
        return self.get_complete_multipartite_k_hgs()


k = 3
vertex_set = [1, 2, 3, 4]

a = CompleteMultipartiteFactory(k, vertex_set).get_hypergraphs()
for b in a:
    print(b)
