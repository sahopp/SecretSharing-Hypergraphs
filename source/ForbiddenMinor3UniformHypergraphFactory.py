from HypergraphFactory import *
from helpers import *


class ForbiddenMinor3UniformHypergraphFactory(HypergraphFactory):
    def __init__(self, v_set):
        assert len(set(v_set)) == 5
        self.v_set = v_set
        self.forbidden_minors = []

        # PHI
        self.forbidden_minors.append({"minor": [[v_set[0], v_set[1], v_set[4]], [v_set[1], v_set[2], v_set[4]], [v_set[2], v_set[3], v_set[4]]],
                                      "super_he": [[v_set[0], v_set[1], v_set[2]], [v_set[0], v_set[1], v_set[3]], [v_set[0], v_set[2], v_set[3]], [v_set[1], v_set[2], v_set[3]]]})
        # PHI HAT
        self.forbidden_minors.append({"minor": [[v_set[0], v_set[1], v_set[4]], [v_set[1], v_set[2], v_set[4]], [v_set[2], v_set[3], v_set[4]], [v_set[1], v_set[3], v_set[4]]],
                                      "super_he": [[v_set[0], v_set[1], v_set[2]], [v_set[0], v_set[1], v_set[3]], [v_set[0], v_set[2], v_set[3]], [v_set[1], v_set[2], v_set[3]]]})
        # PHI HAT STAR
        self.forbidden_minors.append({"minor": [[v_set[0], v_set[1], v_set[2]], [v_set[0], v_set[3], v_set[4]], [v_set[1], v_set[3], v_set[4]]],
                                      "super_he": [[v_set[0], v_set[1], v_set[3]], [v_set[0], v_set[2], v_set[3]], [v_set[1], v_set[2], v_set[3]]]})
        # PSI3
        self.forbidden_minors.append({"minor": [[v_set[0], v_set[1], v_set[2]], [v_set[0], v_set[3], v_set[4]], [v_set[1], v_set[3], v_set[4]], [v_set[2], v_set[3], v_set[4]]],
                                      "super_he": [[v_set[0], v_set[1], v_set[3]], [v_set[0], v_set[2], v_set[3]], [v_set[1], v_set[2], v_set[3]]]})

    def get_hgs_with_forbidden_minors(self):
        forbidden_hgs = []
        for fm in self.forbidden_minors:
            for he_set in powerset(fm["super_he"]):
                forbidden_hgs.append(fm["minor"] + he_set)
        return forbidden_hgs

    def get_hypergraphs(self):
        return self.get_hgs_with_forbidden_minors()
