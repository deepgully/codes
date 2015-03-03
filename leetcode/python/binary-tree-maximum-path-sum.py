"""
https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/

Binary Tree Maximum Path Sum  

Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

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

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root is None:
            return 0
        
        self.max_sum = None
        
        def max2(n1, n2):
            if n1 is None:
                return n2
            if n2 is None:
                return n1
                
            return max(n1, n2)        
        
        def max_path_sum(node):
            if node is None:
                return 0
                
            left_sum = max2(0, max_path_sum(node.left))
            right_sum = max2(0, max_path_sum(node.right))
            
            self.max_sum = max2(self.max_sum, left_sum + right_sum + node.val)
            
            return node.val + max2(left_sum, right_sum)
            
        max_path_sum(root)
        
        return self.max_sum or 0
        
        
def test_main():
    trees = [
        "{1,2,3,4,5,6,7,-8,9,10,11,12,13,14}",
        "{3,9,-20,#,#,15,7}",
        "{1,2,-3,#,#,4,#,#,5}",
        "{1,2,2,3,-4,4,3}",
        "{1,2,2,#,3,#,3}",
        "{1,2,-2,3,#,#,3}",
        "{1,2}",
        "{1,#,2}",
        "{1,2,3}",
        "{1,#,-2,3}",
        "{#}",
        "{1}",
        "{}",
        str(range(20)),
        "{1,#,2,-3,#,4}",
        "{1,#,2,#,3,#,4,#,5,#,-6,#,7,#,8}",
        "{1,#,-2,-3}",
    ]
    
    sol = Solution()
    
    for str_tree in trees:
        print("\nload str tree:")
        print(str_tree)
        tree_root = loads_level_order(str_tree)
        print("dump str tree:")
        print(dumps_level_order(tree_root))
                                     
        print("answer: %s" % sol.maxPathSum(tree_root))
   
if __name__ == "__main__":
    test_main()
