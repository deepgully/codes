"""
https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/

Minimum Depth of Binary Tree 

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import level_order_iter
from support import loads_level_order, dumps_level_order

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        
        min_depth = 0
        for node, depth in level_order_iter(root, False):
            if node.left is None and node.right is None:
                return depth + 1
            else:
                min_depth = depth + 1
            
        return min_depth
        
        
def test_main():
    sol = Solution()

    def test(str_tree):
        print("\nload str tree:")
        print(str_tree)
        tree_root = loads_level_order(str_tree)
        print("dump str tree:")
        print(dumps_level_order(tree_root))
                
        print("minDepth: %s" % sol.minDepth(tree_root))
    
    trees = [
        "{1,2,3,4,5,6,7,8,9,10,11,12,13,14}",
        "{3,9,20,#,#,15,7}",
        "{1,2,3,#,#,4,#,#,5}",
        "{1,2,2,3,4,4,3}",
        #"{1,2,2,#,3,#,3}",
        "{1,2,2,3,#,#,3}",
        "{1,2}",
        "{1,#,2}",
        "{1,2,3}",
        "{1,#,2,3}",
        "{#}",
        "{1}",
        "{}",
        "{1,#,2,#,3,#,4,#,5,#,6,#,7,#,8}",
        "{1,2,#,3,#,4,#,5,#,6,#,7,#,8}",
    ]

    for s in trees:
        test(s)

        
if __name__ == "__main__":
    test_main()
