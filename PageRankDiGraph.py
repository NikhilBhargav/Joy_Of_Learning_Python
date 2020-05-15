# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:44:40 2020

@author: Nikhil Bhargava

Page rank convergence of weight
"""
import networkx as nx
import random
import matplotlib.pyplot as plt 


numNodes=10
seed=100
maxIterations=1000


#Add Edges
def add_edges():
    nodes=list(G.nodes())
    
    for s in nodes:
        for t in nodes:
            #Don't create loop. Create simple randomized graph
            if(s!=t):
                r=random.random()
                if(r<0.5):
                    G.add_edge(s,t)                            
    return G

def assign_points(G):    
    nodes=list(G.nodes())
    p=[]
    for each in nodes:
        p.append(seed)
    return p

def distribute_points(G, points):
    nodes=list(G.nodes())
    new_points=[]
    for i in range(len(nodes)):
        new_points.append(0)
        
    for n in nodes:
        out=list(G.out_edges(n))
        
        #n is sink
        if(len(out)==0):
            new_points[n]=new_points[n]+points[n]
        else:
            share=points[n]/len(out)
            for (src,tgt) in out:
                new_points[tgt]=new_points[tgt]+share
                
    return(new_points)
    

def keep_distributing(points,G):
    i=0
    while(i<maxIterations):
        new_points=distribute_points(G,points)
        #print(new_points)
        points=new_points
        i=i+1
    return (new_points)
    
    
def rank_by_points(points):
    d={}
    for i in range(len(points)):
        d[i]=points[i]
        
    print("Page rank by our method")
    print(sorted(d.items(), key=lambda f:f[1]))
    
#Create a DIGRAPH
G=nx.DiGraph()
G.add_nodes_from([i for i in range(numNodes)])
G=add_edges()

#Visualize the graph
nx.draw(G, with_labels=True)
plt.show()

#Assign initial points
points=assign_points(G)

#Distribute the points
final_points=keep_distributing(points,G)

#Rank by points
rank_by_points(final_points)

#default networkx function pagerank
res=nx.pagerank(G)

#Sort the points dict
print("Page rank by Networkx library PageRank method")
print(sorted(res.items(), key=lambda f:f[1]))