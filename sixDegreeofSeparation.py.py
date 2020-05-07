####
## Six degrees of Sepratation in python
####
import networkx as nx
import numpy as np

G=nx.gnp_random_graph(50,0.3)

#G=nx.read_edgelist("facebook_combined.txt")

#Find all nodes
Node=list(G.nodes())

#Shortest path linklist
spll=[]

for u in Node:
	for v in Node:
		if(u!=v):
			l=nx.shortest_path_length(G,u,v)
			print("Shortest path b/w ",u," and ",v" is ",l)
			spll.append(l)
		
#Minand MAx Shortest path in G		
min_spl=min(spll)
max_spl=max(spll)

#Average shortest path in G 
avg_spl=np.average(spll)

print("Min spl:",min_spl," Max spl:",max_spl," and Avg spl:", avg_spl)

