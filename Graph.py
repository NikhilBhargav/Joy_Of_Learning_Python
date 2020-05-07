####
## Graph in python
####

import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(3,4)

print (G.nodes())
print (G.edges())

#Draw Graph
nx.draw(G)
plt.show