import networkx as nx

with open('Day06/input','r') as f: input = f.read()
g = nx.Graph()
g.add_edges_from(x.split(')') for x in input.split('\n'))
print(nx.shortest_path_length(g, 'YOU', 'SAN') - 2)