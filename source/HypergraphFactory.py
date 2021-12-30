from abc import ABC, abstractmethod, abstractclassmethod
import itertools


class HypergraphFactory(ABC):
    def _subset_sum_rec(self, min_parts, numbers, target, partial, results):
        if partial is None:
            partial = []
        s = sum(partial)

        # check if the partial sum is equal to target and there are at least min_parts parts
        if s == target and len(partial) >= min_parts:
            results += [partial]
        if s >= target:
            return

        for i in range(len(numbers)):
            n = numbers[i]
            remaining = numbers[i:]
            self._subset_sum_rec(min_parts, remaining, target, partial + [n], results)
        return results

    @abstractmethod
    def get_hypergraphs(self):
        pass
