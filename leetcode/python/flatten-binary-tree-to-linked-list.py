"""
https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/

Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

Hints:
If you notice carefully in the flattened tree, 
each node's right child points to the next node of a pre-order traversal.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import pre_order_iter
from support import loads_level_order, dumps_level_order

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return 
                        
        flatten_nodes = [node for node, depth in pre_order_iter(root)]
        
        for i in xrange(len(flatten_nodes)-1):
            flatten_nodes[i].left = None
            flatten_nodes[i].right = flatten_nodes[i+1]
            
        flatten_nodes[-1].left = None
        flatten_nodes[-1].right = None
        
        return flatten_nodes[0]
       
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten2(self, root):
        if not root:
            return 
                   
        while root is not None:
            if root.left is None:
                root = root.right
                continue
                
            left_node = root.left
            while left_node.right is not None:
                left_node = left_node.right
                
            left_node.right = root.right
            root.right = root.left
            root.left = None
            
            root = root.right
        
        
def test_main():
    import random
    
    sol = Solution()

    def test(str_tree):
        print("\nload str tree:")
        print(str_tree)
        tree_root = loads_level_order(str_tree)
        print("dump str tree:")
        print(dumps_level_order(tree_root))
               
        sol.flatten(tree_root)
        
        print("dump str tree after flatten:")
        print(dumps_level_order(tree_root))
        
        tree_root = loads_level_order(str_tree)
        
        sol.flatten2(tree_root)
        
        print("dump str tree after flatten2:")
        print(dumps_level_order(tree_root))
            
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
