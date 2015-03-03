"""
https://oj.leetcode.com/problems/word-ladder-ii/

Word Ladder II 

Given two words (start and end), and a dictionary, 
find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""

from support import collections

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        """ http://interactivepython.org/courselib/static/pythonds/Graphs/graphbfs.html """
        if not dict:
            return [] 
                
        if len(start) != len(end):
            return []
                    
        def build_graph(words):
            """ build no-ordered graph from words """
            mapping = collections.defaultdict(set)
            
            for word in words:
                for idx in xrange(len(word)):
                    bucket = word[:idx] + "?" + word[idx+1:]
                            
                    mapping[bucket].add(word)
                                         
            graph = collections.defaultdict(set)
            
            for bucket, words in mapping.iteritems():
                for word1 in words:
                    for word2 in words:
                        if word1 != word2:
                            graph[word1].add(word2)
                            graph[word2].add(word1)
                            
            return graph
                        
        def bfs(g, start, end):
            """ find all shortest paths from start to end """
            short_paths = []
            
            cur_depth = 1
            cur_depth_nodes = []    # save visited nodes for current depth
            visited_nodes = set()   # save all visited nodes
            
            queue = collections.deque()
            queue.append([start])
            
            while queue:
                path = queue.popleft()
                
                if len(path) > cur_depth: 
                    # search done on current depth, move to next depth
                    cur_depth = len(path)
                    
                    # add nodes from last depth in visited list
                    visited_nodes.update(set(cur_depth_nodes))
                    
                    cur_depth_nodes = []  # reset add nodes for current depth
                    
                if short_paths and cur_depth + 1 > len(short_paths[0]):
                    # break out if depth > length of shortest path
                    break
                                
                # scan the last vertex in path
                vertex = path[-1]
                for nbr in g.get(vertex, []):  
                    if nbr == end:
                        short_paths.append(path + [nbr])
                    
                    if nbr not in visited_nodes:   
                        # add new path in queue
                        queue.append(path + [nbr])
                        # add visited node
                        cur_depth_nodes.append(nbr)  
                                           
            return short_paths
        
        dict = set(dict)
        dict.add(start)
        dict.add(end)
        
        graph = build_graph(dict)
        
        return bfs(graph, start, end)
        

def test_main():
    sol = Solution()

    input = [
        ("a", "c", ["a", "b", "c"]),
        ("hit", "cog", ["hot","dot","dog","lot","log"]),
        ("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]), 
        # [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]

    ]

    for s in input:
        print(s)
        print(sol.findLadders(*s))


if __name__ == "__main__":
    test_main()
    