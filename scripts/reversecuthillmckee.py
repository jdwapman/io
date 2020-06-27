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
        cooMatrix = csrMatrix.tocoo()
    else:
        if not inputFile:
            inputFile = sys.stdin

        cooMatrix = mmread(inputFile)  # returns coo_matrix
        csrMatrix = cooMatrix.tocsr()

    if visFile:
        (dim, dimtemp) = csrMatrix.shape
        assert dim == dimtemp
        # array = csrMatrix.toarray()
        # array = array.astype(bool).astype(int)  # now 0s and 1s only
        # downscale: every downscale x downscale subarray -> one element
        downscale = dim // 1024
        if useTest:
            downscale = 2
        visdim = ceil(float(dim) / float(downscale))
        # create a new array
        visarray = np.ndarray(shape=(visdim, visdim), dtype="int")  # nnz
        imarray = np.ndarray(shape=(visdim, visdim), dtype="uint8")  # int [0,255]
        for x in range(visdim):
            for y in range(visdim):
                subarray = (
                    csrMatrix[
                        np.array(range(x * downscale, min((x + 1) * downscale, dim))), :
                    ][:, np.array(range(y * downscale, min((y + 1) * downscale, dim)))]
                    .toarray()
                    .astype(bool)  # non-zeroes become 1
                    .astype(int)  # and then turn that 1 back to an int
                )
                visarray[x, y] = np.sum(subarray)
        vismax = float(np.max(visarray))
        for x in range(visdim):
            for y in range(visdim):
                # max value gets black (0.0), min value gets white (255.0)
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
    # this else clause doesn't work, ignore it for now
    # else:
    #     sys.stdout.write(rcmMatrix)


if __name__ == "__main__":
    main(sys.argv[1:])
