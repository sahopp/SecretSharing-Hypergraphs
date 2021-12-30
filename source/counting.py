import itertools
from helpers import *
from CompleteMultipartiteFactory import *
from L12Factory import *


nr_vertices = 5

vertices = list(range(0, nr_vertices))
permutations = list(itertools.permutations(vertices))

forbidden_hashes = set()
ideal_hashes = set()
all_hashes = set()

nr_perm = len(permutations)
cnt = 0

for p in permutations:
    cnt += 1
    print("Permuatation " + str(cnt) + "/" + str(nr_perm) + "\r")

    ############## FORBIDDEN ##############
    forbidden_hgs = []

    ####### PSI_3 #######
    forbidden_minor = [[p[0], p[1], p[2]], [p[0], p[3], p[4]], [p[1], p[3], p[4]], [p[2], p[3], p[4]]]
    super_hyperedges = powerset([[p[0], p[1], p[3]], [p[0], p[2], p[3]], [p[1], p[2], p[3]]])

    for he_set in super_hyperedges:
        forbidden_hgs.append(forbidden_minor + he_set)

    ####### PHI hat star #######
    forbidden_minor = [[p[0], p[1], p[2]], [p[0], p[3], p[4]], [p[1], p[3], p[4]]]
    super_hyperedges = powerset([[p[0], p[1], p[3]], [p[0], p[2], p[3]], [p[1], p[2], p[3]]])

    for he_set in super_hyperedges:
        forbidden_hgs.append(forbidden_minor + he_set)

    ####### PHI #######
    forbidden_minor = [[p[0], p[1], p[4]], [p[1], p[2], p[4]], [p[2], p[3], p[4]]]
    super_hyperedges = powerset([[p[0], p[1], p[2]], [p[0], p[1], p[3]], [p[0], p[2], p[3]], [p[1], p[2], p[3]]])

    for he_set in super_hyperedges:
        forbidden_hgs.append(forbidden_minor + he_set)

    ####### PHI hat #######
    forbidden_minor = [[p[0], p[1], p[4]], [p[1], p[2], p[4]], [p[2], p[3], p[4]], [p[1], p[3], p[4]]]
    super_hyperedges = powerset([[p[0], p[1], p[2]], [p[0], p[1], p[3]], [p[0], p[2], p[3]], [p[1], p[2], p[3]]])

    for he_set in super_hyperedges:
        forbidden_hgs.append(forbidden_minor + he_set)

    # Compute hashes
    for hg in forbidden_hgs:
        forbidden_hashes.add(hg_hash(hg))

    ############## IDEAL ##############
    ideal_hgs = CompleteMultipartiteFactory(3, p).get_hypergraphs() + L12Factory(p).get_hypergraphs()

    # Compute hashes
    for hg in ideal_hgs:
        ideal_hashes.add(hg_hash(hg))

total_hashes = ideal_hashes.union(forbidden_hashes)
all_HGs = powerset(subsets_of_cardinality(vertices, 3))

for hg in all_HGs:
    h = 0
    if covers_n_vertices(hg, nr_vertices):
        h = hg_hash(hg)
        all_hashes.add(h)
        if h not in total_hashes:
            print("Not characterized: " + str(hg))

print("\n")
print("Nr. of HGs in total:             " + str(len(all_hashes)))
print("Nr. of HGs with forbidden minor: " + str(len(forbidden_hashes)))
print("Nr. of known ideal HGs:          " + str(len(set(ideal_hashes))))
print("Nr. of characterized HGs:        " + str(len(total_hashes)))
print("Nr. of non-characterized HGs:    " + str(len(all_hashes) - len(total_hashes)))
