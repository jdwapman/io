#!/usr/bin/env python

#assume io repo's root path is at the same level as gunrock and gunrock_build
import os

social_networks = ['soc-orkut',
                'hollywood-2009',
                'indochina-2004',
                'kron_g500-logn21']
road_networks = ['rgg_n_2_24_s0',
                'roadNet-CA']

options = {
    "direction_optimizing_bfs" : "--src=0 --undirected --idempotence --alpha=2 --beta=2 --queue-sizing=1.5 --queue-sizing1=1.5",
    "breadth_first_search" : "--src=0 --undirected --idempotence --disable-size-check",
    "betweenness_centrality": "--src=0",
    "connected_component": "",
    "pagerank": "--undirected --quick --max-iter=1",
    "single_source_shortest_path": "--src=0 --undirected --idempotence --delta-factor=32",
}


'''for dataset in social_networks:
    for binary in ["direction_optimizing_bfs",
                   "betweenness_centrality",
                   "connected_component",
                   "pagerank",
                   "single_source_shortest_path"]:
        os.system("../../gunrock_build/bin/%s market ../../gunrock/dataset/large/%s/%s.mtx %s --iteration-num=10 --quiet --jsondir=." % (binary, dataset, dataset, options[binary]))'''

for dataset in road_networks:
    for binary in ["breadth_first_search",
                   "single_source_shortest_path"]:
        os.system("../../gunrock_build/bin/%s market ../../gunrock/dataset/large/%s/%s.mtx %s --iteration-num=10 --traversal-mode=1 --quiet --jsondir=." % (binary, dataset, dataset, options[binary]))
    for binary in ["betweenness_centrality",
                   "connected_component",
                   "pagerank"]:
        os.system("../../gunrock_build/bin/%s market ../../gunrock/dataset/large/%s/%s.mtx %s --iteration-num=10 --quiet --jsondir=." % (binary, dataset, dataset, options[binary]))
