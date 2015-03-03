"""
https://oj.leetcode.com/problems/recover-binary-search-tree/

Recover Binary Search Tree 

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import bst_create, rand_list
from support import in_order_traversal, print_node
        
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):               
        self.pre_node = None
        self.err_node1 = None
        self.err_node2 = None
        
        def check_node(node, depth):
            
            if self.pre_node is not None and node.val < self.pre_node.val:
                if self.err_node1 is None:
                    self.err_node1 = self.pre_node
                    self.err_node2 = node
                else:
                    self.err_node2 = node
                    
            self.pre_node = node
        
           
        # start traverse in-order
        in_order_traversal(root, check_node)
        
        if self.err_node1 is not None and self.err_node2 is not None:
            self.err_node1.val, self.err_node2.val = self.err_node2.val, self.err_node1.val
        
        return root

        
def test_main():
    sol = Solution()
    
    for i in xrange(10):
        tree = bst_create(rand_list(i))
        
        print("old tree")
        in_order_traversal(tree, print_node)
        
        if tree and tree.left and tree.right:
            tree.right.val, tree.left.val = tree.left.val, tree.right.val
        
        print("changed tree")
        in_order_traversal(tree, print_node)

        new_tree = sol.recoverTree(tree)
        print("recovered tree")
        in_order_traversal(new_tree, print_node)

if __name__ == "__main__":
    test_main()
