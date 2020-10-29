#!/usr/bin/env python

import numpy as np
import networkx as nx
import sys, getopt
from scipy.io import mmread, mmwrite
from scipy.sparse.csgraph import reverse_cuthill_mckee
from scipy.sparse import csr_matrix


def main(argv):

    if len(argv) != 2:
        print("Usage: ./graph_compare.py [graph1.mtx] [graph2.mtx]")
        sys.exit()

    graph1 = argv[0]
    graph2 = argv[1]

    graph1_coo = mmread(graph1)
    graph2_coo = mmread(graph2)

    print("Graph 1: ", graph1)
    print("Graph 2: ", graph2)

    graph1 = nx.DiGraph(nx.from_scipy_sparse_matrix(graph1_coo))
    graph2 = nx.DiGraph(nx.from_scipy_sparse_matrix(graph2_coo)) 

    # Check same number of nodes
    print("|V| matches: ", graph1.number_of_nodes() == graph2.number_of_nodes())

    # Check same number of edges
    print("|E| matches: ", graph1.number_of_edges() == graph2.number_of_edges())

    # Check degree histogram matches
    degrees_1 = np.zeros(graph1.number_of_nodes())
    degrees_2 = np.zeros(graph2.number_of_nodes())
    for v in graph1:
        for nbr in graph1[v]:
            degrees_1[v] += 1
    for v in graph2:
        for nbr in graph1[v]:
            degrees_2[v] += 1

    np.sort(degrees_1)
    np.sort(degrees_2)

    print("Degrees match: ", np.sum(degrees_1 - degrees_2) == 0)

    # Check nx RCM matches scipy rcm
    scipy_rcm_1 = reverse_cuthill_mckee(csr_matrix(graph1_coo))
    scipy_rcm_2 = reverse_cuthill_mckee(csr_matrix(graph2_coo))

    nx_rcm_1 = nx.utils.reverse_cuthill_mckee_ordering(graph1)
    nx_rcm_2 = nx.utils.reverse_cuthill_mckee_ordering(graph2)

if __name__ == "__main__":
    main(sys.argv[1:])