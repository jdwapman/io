#!/usr/bin/env python3

from math import ceil, floor
import numpy as np
from PIL import Image
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import reverse_cuthill_mckee
from scipy.io import mminfo, mmread, mmwrite
import sys, getopt


def main(argv):
    inputFile = ""
    outputFile = ""
    visFile = ""
    useTest = False
    debug = False
    symmetry = None

    try:
        opts, args = getopt.getopt(argv, "dhi:o:s:tv:")
    except getopt.GetoptError:
        print(
            "{argv[0]} [-d] [-t] [-i <inputfile>] [-s <symmetry>] [-o <outputfile>] [-v <visfile>]"
        )
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print(
                "{argv[0]} [-d] [-t] [-i <inputfile>] [-s <symmetry>] [-o <outputfile>] [-v <visfile>]"
            )
            sys.exit()
        elif opt == "-d":
            debug = True
        elif opt == "-t":
            useTest = True
        elif opt == "-s":
            symmetry = arg
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg
        elif opt in ("-v", "--visfile"):
            visFile = arg

    if useTest:
        # https://www.geeksforgeeks.org/reverse-cuthill-mckee-algorithm/
        csrMatrix = csr_matrix(
            [
                [0, 3, 0, 0, 0, 0, 1, 0, 1, 0],
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

    if visFile:
        array = csrMatrix.toarray()
        (dim, dimtemp) = array.shape
        assert dim == dimtemp
        array = array.astype(bool).astype(int)  # now 0s and 1s only
        # downscale: every downscale x downscale subarray -> one element
        downscale = dim // 1024
        visx = ceil(float(dim) / float(downscale))
        # create a new array
        visarray = np.ndarray(shape=(visx, visx), dtype="int")
        imarray = np.ndarray(shape=(visx, visx), dtype="uint8")
        for x in range(visx):
            for y in range(visx):
                visarray[x, y] = np.sum(
                    array[
                        x * downscale : (x + 1) * downscale,
                        y * downscale : (y + 1) * downscale,
                    ]
                )
        vismax = float(np.max(visarray))
        for x in range(visx):
            for y in range(visx):
                imarray[x, y] = floor(255.0 * (1.0 - (float(visarray[x, y]) / vismax)))
        im = Image.fromarray(imarray)
        print(im.format, im.size, im.mode)
        im.save(visFile)

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
        mmwrite(outputFile, rcmMatrix, symmetry=symmetry)  # , symmetry="general")
    else:
        sys.stdout.write(rcmMatrix)


if __name__ == "__main__":
    main(sys.argv[1:])
