"""
https://oj.leetcode.com/problems/clone-graph/

Clone Graph  

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
         
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""

from support import print_node
from support import recursive_dfs, iterative_dfs
from support import UndirectedGraphNode


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
                        
        new_root = UndirectedGraphNode(node.label)
        
        visited = {
            node: new_root,
        }
        waiting_for_visit = [node]
        
        while waiting_for_visit:
            next = []
            for cur_node in waiting_for_visit:
                for neighbor in cur_node.neighbors:
                    if neighbor not in visited:
                        new_node = UndirectedGraphNode(neighbor.label)
                        next.append(neighbor)
        
                        visited[cur_node].neighbors.append(new_node)
                        
                        visited[neighbor] = new_node
                    else:
                        visited[cur_node].neighbors.append(visited[neighbor])
            
            waiting_for_visit = next

        return new_root
        

def test_main():
    graph = []

    for i in xrange(10):
        graph.append(UndirectedGraphNode(i))
        
    graph[0].neighbors = [graph[3], graph[2], graph[1]]
    graph[1].neighbors = [graph[2]]
    graph[2].neighbors = [graph[2], graph[4]]
    graph[4].neighbors = [graph[0], graph[5]]
    graph[5].neighbors = [graph[7], graph[6]]
    graph[7].neighbors = [graph[8]]
    graph[8].neighbors = [graph[9]]
                
    print("Old Graph:")
    recursive_dfs(graph[0], None, print_node)

    new_graph = Solution().cloneGraph(graph[0])
    print("Clone Graph:")
    iterative_dfs(new_graph, None, print_node)

    
if __name__ == "__main__":   
    test_main()
