"""
https://oj.leetcode.com/problems/insertion-sort-list/

Insertion Sort List 

Sort a linked list using insertion sort.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.
"""

from support import rand_list, ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return None
            
        sorted = ListNode(-1)            
        sorted.next = head  # move head to sorted list
        
        node = head   

        while node.next:  # start from 2nd node
            next_node = node.next
            if next_node.val < node.val:
                sorted_pos = sorted
                while sorted_pos.next.val < next_node.val:
                    sorted_pos = sorted_pos.next
                                    
                node.next = next_node.next
                next_node.next = sorted_pos.next
                sorted_pos.next = next_node
            else:
                node = next_node
        
        return sorted.next
       
        
def test_main():
    for i in xrange(10):
        numbers = rand_list(10)
        print(numbers)
        sol = Solution()
        
        head = ListNode.create_list(items=numbers)
        
        head = sol.insertionSortList(head)
        
        for node in head:
            print node.val, ",", 
        print
    
if __name__ == "__main__":
    test_main()

