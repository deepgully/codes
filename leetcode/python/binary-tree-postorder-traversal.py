"""
https://oj.leetcode.com/problems/binary-tree-postorder-traversal/

Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""

from support import loads_level_order, dumps_level_order
from support import post_order_iter, post_order_traversal

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        return [node.val for node, depth in post_order_iter(root)]
        
    def postorderTraversal2(self, root):
        res = []
        def append_node(node, depth):
            res.append(node.val)
            
        post_order_traversal(root, append_node)
        
        return res
            

def test_main():
    sol = Solution()

    def test(str_tree):
        print("\nload str tree:")
        print(str_tree)
        tree_root = loads_level_order(str_tree)
        print("dump str tree:")
        print(dumps_level_order(tree_root))
                                     
        print("post order: %s" % sol.postorderTraversal(tree_root))
        print("post order: %s" % sol.postorderTraversal2(tree_root))
        
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
        "{1,#,2,3}",
    ]

    for s in trees:
        test(s)
    
    
if __name__ == "__main__":
    test_main()

        