"""
https://oj.leetcode.com/problems/path-sum/

Path Sum  

Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import pre_order_iter, level_order_iter
from support import loads_level_order, dumps_level_order

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        
        def is_leaf_sum(node, sum):
            return node.left is None and node.right is None and node.val == sum
        
        for node, depth in level_order_iter(root):   # or pre_order_iter
            if is_leaf_sum(node, sum):
                return True
        
            if node.left is not None:
                node.left.val += node.val
                if is_leaf_sum(node.left, sum):  # speed up
                    return True
                
            if node.right is not None:
                node.right.val += node.val
                if is_leaf_sum(node.right, sum): # speed up
                    return True
        
        return False
        
def test_main():
    import random
    
    sol = Solution()

    def test(str_tree):
        print("\nload str tree:")
        print(str_tree)
        tree_root = loads_level_order(str_tree)
        print("dump str tree:")
        print(dumps_level_order(tree_root))
        
        target = random.randint(5, 10)
                
        print("hasPathSum %s: %s" % (target, sol.hasPathSum(tree_root, target)))
    
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
