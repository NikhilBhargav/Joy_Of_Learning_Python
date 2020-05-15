# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Nikhil Bhargava
Page Rank Algorithm implementation using Random Walk of 10 nodes wiht 0.4 prob
"""
#import required lib
import networkx as nx
import random
import matplotlib.pyplot as plt
import operator


maxIteration=100000
numberofNodes=10
graphDensity=0.4

G=nx.gnp_random_graph(numberofNodes,graphDensity,directed=True)

#Pick random source node to start
node=random.choice([i for i in range(G.number_of_nodes())])
                    
#dictionary to hold count of each node visited                    
dict_counter={}

#initialize all nodes counters to 0
for i in range(G.number_of_nodes()):
    dict_counter[i]=0
    
dict_counter[node]=dict_counter[node]+1

for i in range(maxIteration):
    listNeighbor=list(G.neighbors(node))    
    
    #Check if x is a sink node or not
    if(len(listNeighbor)==0):
        node=random.choice([i for i in range(G.number_of_nodes())])
        dict_counter[node]=dict_counter[node]+1
    else: #Normal node
        #Choose a random neoghbour of node
        node=random.choice(listNeighbor)
        dict_counter[node]=dict_counter[node]+1

p=nx.pagerank(G)
sorted_p=sorted(p.items(),key=operator.itemgetter(1))
sorted_rw=sorted(dict_counter.items(),key=operator.itemgetter(1))
print (sorted_p)
print(sorted_rw)

nx.draw(G,with_labels=True)
plt.show()