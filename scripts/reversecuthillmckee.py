#!/usr/bin/env python3

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import reverse_cuthill_mckee
from scipy.io import mminfo, mmread, mmwrite
import sys, getopt


def main(argv):
    inputFile = ""
    outputFile = ""
    useTest = False
    debug = False

    try:
        opts, args = getopt.getopt(argv, "dhi:o:t", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print("{argv[0]} -i <inputfile> -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print(f"{argv[0]} -i <inputfile> -o <outputfile>")
            sys.exit()
        elif opt == "-d":
            debug = True
        elif opt == "-t":
            useTest = True
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg

    if useTest:
        # https://www.geeksforgeeks.org/reverse-cuthill-mckee-algorithm/
        csrMatrix = csr_matrix(
            [
                [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
                [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
                [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            ]
        )
        # I believe the answer is
        # [[0 1 1 0 0 0 0 0 0 0]
        #  [1 0 0 1 0 0 1 0 0 0]
        #  [1 0 0 0 0 1 0 1 0 0]
        #  [0 1 0 0 1 0 0 1 0 0]
        #  [0 0 0 1 0 0 0 1 0 0]
        #  [0 0 1 0 0 0 1 1 1 0]
        #  [0 1 0 0 0 1 0 0 1 0]
        #  [0 0 1 1 1 1 0 0 0 1]
        #  [0 0 0 0 0 1 1 0 0 1]
        #  [0 0 0 0 0 0 0 1 1 0]]
        # I can't promise this is RCM-correct, but it's the same graph.
        # Note it's symmetric, and mmwrite will output only the lower triangle
    else:
        if not inputFile:
            inputFile = sys.stdin

        cooMatrix = mmread(inputFile)  # returns coo_matrix
        csrMatrix = cooMatrix.tocsr()

    # Returns the permutation array that orders a sparse CSR or CSC matrix in Reverse-Cuthill McKee ordering.
    # https://scicomp.stackexchange.com/questions/24817/applying-the-result-of-cuthill-mckee-in-scipy   couldn't make that work
    # instead used https://github.com/brightway-lca/brightway2-analyzer/blob/master/bw2analyzer/matrix_grapher.py
    perm = reverse_cuthill_mckee(csrMatrix)
    if debug:
        print(f"Here's my input matrix, called csrMatrix:\n{csrMatrix.toarray()}")
        print(f"Then I call perm = reverse_cuthill_mckee(csrMatrix)\nperm = {perm}")
        print(f"csrMatrix[perm, :][:, perm]:\n{csrMatrix[perm, :][:, perm].toarray()}")
        print(f"csrMatrix[perm][perm]:\n{csrMatrix[perm][perm].toarray()}")
        print(f"csrMatrix[perm, perm]:\n{csrMatrix[perm, perm]}")
    rcmMatrix = csrMatrix[perm, :][:, perm]

    # now save it

    if outputFile:
        mmwrite(outputFile, rcmMatrix)  # , symmetry="general")
    else:
        sys.stdout.write(rcmMatrix)


if __name__ == "__main__":
    main(sys.argv[1:])
