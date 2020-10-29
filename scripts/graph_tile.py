#!/usr/bin/env python

import numpy as np
from scipy.io import mmread, mmwrite
from scipy.sparse import csr_matrix
import sys

if len(sys.argv) != 3:
    print("Usage: ./graph_tile.py [tile size in elements] [graph.mtx]")
    sys.exit()

tile_size = int(sys.argv[1])

graph = mmread(sys.argv[2]).tocsr()

nnz = graph.nnz
numVertices = graph.shape[0]

tile_start_s = 0
tile_start_d = 0

lookups_untiled = 0
lookups_tiled = 0

while tile_start_s < numVertices:

    tile_stop_s = tile_start_s + tile_size
    tile_stop_s = min(tile_stop_s, numVertices) 

    tile_start_d = 0
    tile_stop_d = 0

    while tile_stop_d < numVertices:
        tile_stop_d = tile_start_d + tile_size
        tile_stop_d = min(tile_stop_d, numVertices)

        print("Tile ", tile_start_s, "-", tile_stop_s, ",", tile_start_d, "-", tile_stop_d)

        tile = graph[tile_start_s:tile_stop_s, tile_start_d:tile_stop_d]

        # Measure the amount of data savings

        # Worst case is total number of dest vertex lookups
        # Optimized case only counts the first occurence of each dest vertex lookup
        lookups_untiled += tile.nnz 
        # print(lookups_untiled)



        lookups_tiled = 0
        cols = tile.indices
        d = dict.fromkeys(cols)

        lookups_tiled += len(d)


        tile_start_d = tile_stop_d

    tile_start_s = tile_stop_s

print("Untiled lookups: ", lookups_untiled)
print("Tiled lookups: ", lookuaaaa 
print("Bandwidth savings: ", lookups_untiled/lookups_tiled)
