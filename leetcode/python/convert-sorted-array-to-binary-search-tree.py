"""
https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Convert Sorted Array to Binary Search Tree 

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import bst_insert
from support import in_order_traversal, print_node
        
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
            
        root = None
        
        length = len(num)
               
        stack = [(0, length-1)]
        
        while stack:
            left, right = stack.pop()
            if left > right:
                continue
                
            center = (left + right) / 2
            root = bst_insert(root, num[center], True)
            
            stack.append((left, center - 1))
            stack.append((center + 1, right))
                    
        return root
        
def test_main():
    sol = Solution()
    
    for i in xrange(10):
        input = range(i) + [i-1]
        center = i / 2
        input[center:center+1] = [input[center], input[center]]
        print(input)
        
        tree = sol.sortedArrayToBST(input)
               
        print("tree")
        in_order_traversal(tree, print_node)

if __name__ == "__main__":
    test_main()
