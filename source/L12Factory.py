from HypergraphFactory import *
from CompleteMultipartiteFactory import *


class L12Factory(HypergraphFactory):
    def __init__(self, v_set):
        assert len(v_set) == len(set(v_set)), 'L12Factory: No duplicated vertices allowed in vertex set'
        assert len(v_set) >= 3, 'L12Factory: Size of vertex set must be at least 3'

        self.v_set = v_set

    def get_L12_hgs(self):
        n = len(self.v_set)
        all_L12 = []
        for C_size in range(1, n - 1):
            center = self.v_set[:C_size]
            graph_vertices = self.v_set[C_size:]
            graph_parts = []
            component_sizes_lists = self.partition_sizes(len(graph_vertices), 2, 1)
            for component_sizes in component_sizes_lists:
                n = 0
                components = []
                for s in component_sizes:
                    a = CompleteMultipartiteFactory(2, graph_vertices[n:n + s]).get_hypergraphs()
                    components.append(a)
                    n += s
                graph_parts += self.all_combinations(components)

            for g in graph_parts:
                new_hg = []
                for c in center:
                    for e in g:
                        new_hg.append([c] + e)
                all_L12.append(new_hg)
        return all_L12

    def all_combinations(self, lst):
        if len(lst) == 1:
            return lst[0]
        l1 = self.all_combinations(lst[1:])
        result = []
        for e in lst[0]:
            for f in l1:
                result.append(e + f)
        return result

    def get_hypergraphs(self):
        return self.get_L12_hgs()
