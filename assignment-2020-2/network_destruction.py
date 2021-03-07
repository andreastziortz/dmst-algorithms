# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:57:10 2020

@author: andreas
"""
from collections import deque
import sys,pprint
def create_neighbors(g):
    neighbors = {}
    for i in g:
        neighbors[i] = len(g[i])
    return neighbors

def dfs_stack(g, node):
    s = []
    visited = [ False ] * len(g)

    s.append(node)
    while len(s) != 0:
        
        c = s.pop()
        
        visited[c] = True
        for v in g[c]:
            if not visited[v]:
                s.append(v)
    return visited

def dijkstra(g, s):
    nodes = g.keys()
    num_nodes = len(nodes)
    MAX_INT = sys.maxsize
    # nitialize array holding path lengths.
    dist = [ MAX_INT ] * num_nodes
    pos = [-1] * num_nodes
    dist[s] = 0
    pos[s] = s
    # Initialize array holding node predecessors.
    pred = [ -1 ] * (num_nodes)
    # Initialize the priority queue; initially it 
    # is just the same with the distance array.
    pq = dist[:]
    
    elements_in_queue = num_nodes 

    while elements_in_queue != 0:
        u = pq.index(min(pq))
        pq[u] = MAX_INT
        elements_in_queue -= 1
        for v in g[u]:
            # If a better path is found,
            # relax the distance and update
            # the priority queue.
            if dist[u] != MAX_INT and dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                pos[v] = v
                pred[v] = u
                pq[v] = dist[v]
    return (pred, dist, pos)

def count_influence(short_path,node,r,neighbors):
    c = 0 
    c1 = 0
    for i in short_path:
        if i == node:
            t = 0
            for j in short_path[node][1]:
                if j == r:
                    k = short_path[node][2][t]
                    l = neighbors[k]
                    c = c + l - 1
                t = t + 1
    for i in short_path:
        if i == node:
            for j in short_path[node][1]:
                if j == 1:
                    c1 = c1 + 1      
    return (c1 - 1) * (c ),node
    
def adjust_neighbors1(g,neighbors,node):
    for i in g[node]:
        neighbors[i] = neighbors[i] - 1
    for i in g[node]:
        for v in g[i]:
            if v == node: 
                g[i].remove(v)
    m = len(g[node])
    k = 1
    while k <= m:
        g[node].pop()
        k = k + 1
            
    return neighbors

def adjust_neighbors2(g,neighbors,node):
    for i in g[node]:
        neighbors[i] = neighbors[i] - 1
        for v in g[i]:
            if v == node:
                g[i].remove(v)
    neighbors.pop(node)
    g.pop(node)
    return neighbors

def find_influences(neighbors,r,n):   
    short_path = {}
    influences = {}
    counter = 1
    while counter <= n:
        for i in g:
            short_path[i] = dijkstra(g,i)
            influences[i] = count_influence(short_path,i,r,neighbors)
        Max = -sys.maxsize
        for i in influences:
            if influences[i][0] > Max or (influences[i][0] == Max and i < Max_pos):
                Max_pos = influences[i][1]
                Max = influences[i][0]
        print(Max_pos,Max)
        neighbors = adjust_neighbors1(g,neighbors,Max_pos)
        counter = counter + 1

def calculate_nodes(n,neighbors):
    counter = 1
    while counter <= n:
        
        Max = -sys.maxsize
        Max_pos = -1
        for i in neighbors:
            if neighbors[i] > Max or (neighbors[i] == Max and i < Max_pos):
                Max_pos = i
                Max = neighbors[i]
        print(Max_pos,Max)
        neighbors = adjust_neighbors2(g,neighbors,Max_pos)
        counter = counter + 1
def read_file(filename):
    with open(filename) as graph_input:
        for line in graph_input:
            # Split line and convert line parts to integers.
            nodes = [int(x) for x in line.split()]
            if len(nodes) != 2:
                continue
            # If a node is not already in the graph
            # we must create a new empty list.
            if nodes[0] not in g:
                g[nodes[0]] = []
            if nodes[1] not in g:
                g[nodes[1]] = []
            # We need to append the "to" node
            # to the existing list for the "from" node.
            g[nodes[0]].append(nodes[1])
            g[nodes[1]].append(nodes[0])
        return g
g = {} 
check = sys.argv[1]
if check == '-r':
    filename = sys.argv[4]
else:
    filename = sys.argv[3]
g = read_file(filename)
e = min(g)

while e != 0:
     g[e - 1] = []
     e = e - 1 

if check == '-r':
    r = int(sys.argv[2])
    n = int(sys.argv[3])
    neighbors = create_neighbors(g)    
    find_influences(neighbors,r,n)
else:
    n = int(sys.argv[2]) 
    neighbors = create_neighbors(g)
    calculate_nodes(n,neighbors)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   

