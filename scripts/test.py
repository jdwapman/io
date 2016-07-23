import create_graph
#a list of all the commands that you would normally use in terminal, including the filename. It is essential that the filename comes first, as that is how it is done in the terminal.
vectors = {'--plottype':'scatter', '--inputpath': '../gunrock-output/', '--outputtype': 'svg', '--engine': 'Gunrock', '--algorithm': 'BFS', '--xaxis': 'nodes_visited', '--yaxis': 'elapsed', '--conds': '{"undirected": True, "mark_predecessors": True}', '--xlabel': 'Nodes Visited', '--ylabel': 'Elapsed Time', '-v':''}
#pass the vectors to the main function of crreate_graph
create_graph.run(vectors)
