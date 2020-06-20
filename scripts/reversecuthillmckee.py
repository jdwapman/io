#!/usr/bin/env python3

from scipy.sparse.csgraph import reverse_cuthill_mckee
from scipy.io import mminfo, mmread, mmwrite
import sys, getopt


def main(argv):
    input_file = ""
    output_file = ""

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print("{argv[0]} -i <inputfile> -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print(f"{argv[0]} -i <inputfile> -o <outputfile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg

    print(input_file, output_file)

    # parse command line
    if not input_file:
        input_file = sys.stdin

    coo_matrix = mmread(input_file)  # returns coo_matrix
    csr_matrix = coo_matrix.tocsr()

    # Returns the permutation array that orders a sparse CSR or CSC matrix in Reverse-Cuthill McKee ordering.
    # https://scicomp.stackexchange.com/questions/24817/applying-the-result-of-cuthill-mckee-in-scipy   couldn't make that work
    # instead used https://github.com/brightway-lca/brightway2-analyzer/blob/master/bw2analyzer/matrix_grapher.py
    perm = reverse_cuthill_mckee(csr_matrix)
    rcm_matrix = csr_matrix[perm, :][:, perm]

    # now save it

    if output_file:
        mmwrite(output_file, rcm_matrix)
    else:
        sys.stdout.write(rcm_matrix)


if __name__ == "__main__":
    main(sys.argv[1:])
