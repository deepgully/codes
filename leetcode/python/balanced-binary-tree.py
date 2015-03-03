"""
https://oj.leetcode.com/problems/balanced-binary-tree/

Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import loads_level_order, dumps_level_order

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def get_depth_and_banlanced(node):
    if not node:
        return 0, True
        
    left, b_left = get_depth_and_banlanced(node.left)
    
    #if not b_left:
    #    return left + 1, False
        
    right, b_right = get_depth_and_banlanced(node.right)
        
    return (max(left, right) + 1, 
            b_left and b_right and abs(left - right) <= 1)
    

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):          
        depth, balanced = get_depth_and_banlanced(root)
        
        return balanced
            
        
def test_main():
    import random
    
    sol = Solution()

    def test(str_tree):
        print("\nload str tree:")
        print(str_tree)
        tree_root = loads_level_order(str_tree)
        print("dump str tree:")
        print(dumps_level_order(tree_root))
                       
        print("isBalanced = %s" % sol.isBalanced(tree_root))
            
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
        "{1,2,2,3,3,3,3,4,4,4,4,4,4,#,#,5,5}",
        "{1,2,2,3,#,#,3,4,#,#,4}",
    ]

    for s in trees:
        test(s)

        
if __name__ == "__main__":
    test_main()
