# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:45:06 2020

@author: andreas
"""
import pprint
import sys

def create_graph(n):
    graph = {}
    for x in range(0,n):
        for y in range(0,n-x):
            graph[x,y] = (x,y)
            if x != 0 and y > 0:
                graph[-x,y]= (-x,y) 
    
    return graph
def create_neighbors(graph):
    Neighbors = {}
    for n in graph:
        Neighbors[n[0],n[1]] = [(n[0]-1,n[1]),(n[0]+1,n[1]),(n[0],n[1]-1),(n[0],n[1]+1)]  
    return Neighbors
def AdjacencyList(graph,u,Neighbors):
    f = []
    for k in Neighbors[u]:
        for l in graph:
            if k == l:
                f.append(k)
                break
    return f
def IsSetEmpty(untried):
    if len(untried) == 0 :
        return True
    else:
        return False
def AppendToList(p,u):
    p.append(u)
    return p
def SizeList(p):
    return len(p)
def find_polyonymesneighbor(p,Neighbors,v,u):
    for i in p:
        if (i != (u[0],u[1])):
            for j in Neighbors[i]:
                if j == v:
                   return False     
    return True
def AddToSet(new_neighbors,v):
    new_neighbors.add(v)
    return new_neighbors
def RemoveFromList(p,u):
    p.remove(u)
    return p
def CountFixedPolyominoes(graph,untried,n,p,Neighbors):
    global c
    while not (IsSetEmpty(untried)):
        u = untried.pop()
        p = AppendToList(p,u)
        if SizeList(p) == n:
            c = c + 1    
        else:
            new_neighbors = set()
            for v in AdjacencyList(graph,u,Neighbors): 
                if v not in untried and v not in p and find_polyonymesneighbor(p,Neighbors,v,u):
                    AddToSet(new_neighbors,v)
            new_untried = untried | new_neighbors
            CountFixedPolyominoes(graph,new_untried,n,p,Neighbors)
        RemoveFromList(p,u)
    return c


c = 0
check = len(sys.argv)

if check == 2:
    n = int(sys.argv[1])
    graph = create_graph(n)
    Neighbors = create_neighbors(graph)
    c = CountFixedPolyominoes(graph,{(0,0)},n,[],Neighbors)
    pprint.pprint(c)
else:
    n = int(sys.argv[2])
    graph = create_graph(n)
    Neighbors = create_neighbors(graph)
    c = CountFixedPolyominoes(graph,{(0,0)},n,[],Neighbors)
    for i in graph:
        graph[i] = AdjacencyList(graph,i,Neighbors)
    pprint.pprint(graph)
    print(c)


