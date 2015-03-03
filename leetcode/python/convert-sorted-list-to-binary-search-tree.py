"""
https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import ListNode, TreeNode
from support import dumps_level_order, in_order_iter

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if not head:
            return
            
        self.cur_node = head
        
        def build_bst(size):
            if size <= 0:
                return None
                
            tree_node = TreeNode(-1)
            tree_node.left = build_bst(size/2)
            tree_node.val = self.cur_node.val
            
            self.cur_node = self.cur_node.next
            
            tree_node.right = build_bst(size - size/2 - 1)
            
            return tree_node
                            
        count = 0
        while head:
            count += 1
            head = head.next
        
        return build_bst(count)
        
    # @param head, a list node
    # @return a tree node
    def sortedListToBST2(self, head):
        if not head:
            return
                   
        def build_bst(nodes):
            if not nodes:
                return None
                
            size = len(nodes)
            center = size/2
            nodes[center].left = build_bst(nodes[:center])
            nodes[center].right = build_bst(nodes[center+1:])
            
            return nodes[center]
            
        tree_nodes = []                           
        while head:
            tree_nodes.append(TreeNode(head.val))
            head = head.next
            
        return build_bst(tree_nodes)
        
        
def test_main():
    import random
    
    sol = Solution()

    for i in xrange(10):
        sorted_list = ListNode.create_list(i)
        for node in sorted_list:
            print(node)
            
        tree = sol.sortedListToBST(sorted_list)
        print("sortedListToBST = %s" % dumps_level_order(tree))
        
        for node,d in in_order_iter(tree):
            print(node)
            
        tree = sol.sortedListToBST2(sorted_list)
        print("sortedListToBST2 = %s" % dumps_level_order(tree))
        
        for node,d in in_order_iter(tree):
            print(node)

        
if __name__ == "__main__":
    test_main()
