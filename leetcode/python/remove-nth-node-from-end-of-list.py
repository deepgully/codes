"""
https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/

Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import ListNode
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head or n < 1:
            return head
            
        way_points = {}
        way_point_count = 10
        
        length = 0
        cur_node = head
        while cur_node is not None:
            if length % way_point_count == 0:
                way_points[length] = cur_node
            length += 1
            cur_node = cur_node.next
            
        if n > length:
            return head
        if n == length:
            return head.next
        
        target = length - n
               
        m, n = target/way_point_count, target % way_point_count
        
        if n == 0:
            m -= 1
            n += way_point_count
            
        start_node = way_points[m * way_point_count]
        cur_node = start_node
        for i in xrange(n-1):  # move to prev node of target
            cur_node = cur_node.next
                  
        cur_node.next = cur_node.next.next
        return head
        
    def removeNthFromEnd(self, head, n):
        if not head or n < 1:
            return head
            
        length = 0
        cur_node = head
        while cur_node is not None:
            length += 1
            cur_node = cur_node.next
            
        if n > length:
            return head
        if n == length:
            return head.next
        
        target = length - n
        
        cur_node = head
        for i in xrange(target-1):  # move to prev node of target
            cur_node = cur_node.next
                  
        cur_node.next = cur_node.next.next
        return head
        


def test_main(passes=10):
    import random
    sol = Solution()
    
    for i in xrange(passes):
        input = ListNode.create_list(items=[0,5,7,9,5,1,3,9,8,7,3,6])

        k = random.randint(0, i)
        
        k = 2
        

        print("\nremoveNthFromEnd %s nodes %s" % (k, input and list(input)))
        new_node = sol.removeNthFromEnd(input, k)

        print("answer:")
        print(new_node and list(new_node))

if __name__ == "__main__":
    test_main()

