import networkx as nx

with open('Day06/input','r') as f: input = f.read()
g = nx.DiGraph()
g.add_edges_from(x.split(')') for x in input.split('\n'))
print(sum(nx.shortest_path_length(g, 'COM').values()))