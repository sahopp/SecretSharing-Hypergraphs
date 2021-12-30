from CompleteMultipartiteFactory import *


class L12Factory(HypergraphFactory):
    def __init__(self, v_set):
        self.v_set = v_set

    def get_L12_hgs(self):
        n = len(self.v_set)
        all_L12 = []
        for C_size in range(1, n - 1):
            C = self.v_set[:C_size]
            graph_vertices = self.v_set[C_size:]
            G = []
            component_sizes_lists = self.partition_sizes(len(graph_vertices), 2, 1)
            for component_sizes in component_sizes_lists:
                n = 0
                components = []
                for s in component_sizes:
                    a = CompleteMultipartiteFactory(2, graph_vertices[n:n + s]).get_hypergraphs()
                    components.append(a)
                    n += s
                G += self.all_combinations(components)

            for g in G:
                new_hg = []
                for c in C:
                    for e in g:
                        new_hg.append([c] + e)
                all_L12.append(new_hg)
        return all_L12

    def all_combinations(self, l):
        if len(l) == 1:
            return l[0]
        l1 = self.all_combinations(l[1:])
        result = []
        for e in l[0]:
            for f in l1:
                result.append(e + f)
        return result

    def get_hypergraphs(self):
        return self.get_L12_hgs()


vertex_set = [1, 2, 3, 4]
a = L12Factory(vertex_set).get_hypergraphs()
for b in a:
    print(b)
