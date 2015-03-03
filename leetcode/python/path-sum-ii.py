"""
https://oj.leetcode.com/problems/path-sum-ii/

Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

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

org_sum = sum

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if not root:
            return []
        
        def is_leaf_sum(node, target):
            if isinstance(node.val, int):
                node.val = [node.val]
                    
            if node.left is None and node.right is None:    
                return org_sum(node.val) == target
                    
            return False
        
        res = []
        for node, depth in pre_order_iter(root):   # or level_order_iter
            if is_leaf_sum(node, sum):
                res.append(node.val)               
            
            if node.left is not None:
                node.left.val = node.val + [node.left.val]
                
            if node.right is not None:
                node.right.val = node.val + [node.right.val]
        
        return res
        
    def pathSum2(self, root, sum):
        """ recursive version """
        node = root
        
        if not node:
            return []
            
        if node.left is None and node.right is None and node.val == sum:
            return [[node.val]]
            
        left_res = self.pathSum2(node.left, sum-node.val)
        right_res = self.pathSum2(node.right, sum-node.val)
        
        return [[node.val] + res for res in left_res+right_res]
        
        
def test_main():
    import random
    
    sol = Solution()

    def test(str_tree):
        print("\nload str tree:")
        print(str_tree)
        tree_root = loads_level_order(str_tree)
        print("dump str tree:")
        print(dumps_level_order(tree_root))
        
        target = random.randint(5, 30)
        
        print("pathSum2 %s: %s" % (target, sol.pathSum2(tree_root, target)))
        print("pathSum %s: %s" % (target, sol.pathSum(tree_root, target)))
    
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
