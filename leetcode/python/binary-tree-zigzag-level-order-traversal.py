"""
https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

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
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
            
        if root.left is None and root.right is None:
            return [[root.val]]
        
                                                   
        zigzag_list = []
        
        for node, depth in level_order_iter(root):
            if len(zigzag_list) <= depth:
                zigzag_list.append([])
                
            if (depth % 2 == 0):
                zigzag_list[depth].append(node.val)
            else:
                zigzag_list[depth].insert(0, node.val)
        
        return zigzag_list
        
        
def test_main():
    sol = Solution()

    def test(str_tree):
        print("\nload str tree:")
        print(str_tree)
        tree_root = loads_level_order(str_tree)
        print("dump str tree:")
        print(dumps_level_order(tree_root))
                                     
        print("zigzag order: %s" % sol.zigzagLevelOrder(tree_root))
    
    trees = [
        "{1,2,3,4,5,6,7,8,9,10,11,12,13,14}",
        "{3,9,20,#,#,15,7}",
        "{1,2,3,#,#,4,#,#,5}",
        "{1,2,2,3,4,4,3}",
        "{1,2,2,#,3,#,3}",
        "{1,2,2,3,#,#,3}",
        "{1,2}",
        "{1,#,2}",
        "{1,2,3}",
        "{1,#,2,3}",
        "{#}",
        "{1}",
        "{}",
        str(range(20)),
        "{1,#,2,3,#,4}",
        "{1,#,2,#,3,#,4,#,5,#,6,#,7,#,8}",
        "{3,9,20,#,#,15,7}",
    ]

    for s in trees:
        test(s)
    
if __name__ == "__main__":   
    test_main()
        