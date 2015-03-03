# -*- coding: utf-8 -*-
"""
Leetcode OJ support lib of graph

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""
import sys
import collections


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
        
    def __repr__(self):
        return "<Node %s: 0x%s> %s" % (self.label, id(self), [n.label for n in self.neighbors])
        
        
def recursive_dfs(start, visited=None, callback=None, cur_depth=0):
    """recursive depth first search from start"""
    if visited is None:
        visited = {}
    
    if callback is not None:
        callback(start, cur_depth)
    
    visited[start] = True
        
    for node in start.neighbors:
        if node not in visited:
            visited = recursive_dfs(node, visited, callback, cur_depth+1)
            
    return visited
    

def iterative_dfs(start, visited=None, callback=None, cur_depth=0):
    """iterative depth first search from start"""
    if visited is None:
        visited = {}
        
    queue = collections.deque()
    queue.append((start, cur_depth))
    
    while queue:
        node, cur_depth = queue.popleft()
        if node not in visited:
            visited[node] = True
            if callback is not None:
                callback(node, cur_depth)
            
            for nbr in reversed(node.neighbors):
                queue.appendleft((nbr, cur_depth+1))         
                

def recursive_bfs(start, visited=None, callback=None, cur_depth=0, queue=None):
    """recursive breadth first search from start"""
    if visited is None:
        visited = {}
        
    if queue is None:
        queue = collections.deque()
        queue.append((start, cur_depth))
    
    if queue:
        node, cur_depth = queue.popleft()
        if node not in visited:
            visited[node] = True
            if callback is not None:
                callback(node, cur_depth)
                
            for nbr in node.neighbors:
                queue.append((nbr, cur_depth+1))
            
        visited = recursive_bfs(None, visited, callback, cur_depth+1, queue)
                
    return visited

    
def iterative_bfs(start, visited=None, callback=None, cur_depth=0):
    """iterative breadth first search from start"""
    if visited is None:
        visited = {}
        
    queue = collections.deque()
    queue.append((start, cur_depth))
    
    while queue:
        node, cur_depth = queue.popleft()
        if node not in visited:
        
            visited[node] = True
            if callback is not None:
                callback(node, cur_depth)
                
            for nbr in node.neighbors:
                queue.append((nbr, cur_depth+1))
                
    return visited
                
            
                
            

        