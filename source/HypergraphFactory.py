from abc import ABC, abstractmethod, abstractclassmethod
from helpers import *

class HypergraphFactory(ABC):
    def partition_sizes(self, nr_vertices, min_part_size, min_part_nr):
        numbers = list(range(min_part_size, nr_vertices + 1))
        return self._subset_sum_rec(min_part_nr, numbers, nr_vertices, [], [])

    def _subset_sum_rec(self, min_parts, numbers, nr_vertices, partial, results):
        s = sum(partial)

        # check if the partial sum is equal to target and there are at least min_parts parts
        if s == nr_vertices and len(partial) >= min_parts:
            results += [partial]
        if s >= nr_vertices:
            return

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i:]
            self._subset_sum_rec(min_parts, remaining, nr_vertices, partial + [n], results)
        return results

    @abstractmethod
    def get_hypergraphs(self):
        pass
