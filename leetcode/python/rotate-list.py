"""
https://oj.leetcode.com/problems/rotate-list/

Rotate List

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

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
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None:
            return None
        if head.next is None:
            return head
        if k <= 0:
            return head

        length = 0
        cur_node = end_node = head
        while cur_node is not None:
            length += 1
            end_node = cur_node
            cur_node = cur_node.next

        if k >= length:
            k = k % length

        i = 1
        # find rotate position
        pre_rotate_pos = head
        while pre_rotate_pos and i < (length-k):
            i += 1
            pre_rotate_pos = pre_rotate_pos.next

        if pre_rotate_pos is not None and pre_rotate_pos.next is not None:
            end_node.next = head
            head = pre_rotate_pos.next
            pre_rotate_pos.next = None

        return head


def test_main(passes=10):
    import random
    sol = Solution()
    
    for i in xrange(passes):
        input = ListNode.create_list(i)

        k = random.randint(0, i)

        print("\n right rotate %s nodes %s" % (k, input and list(input)))
        new_node = sol.rotateRight(input, k)

        print("answer:")
        print(new_node and list(new_node))

if __name__ == "__main__":
    test_main()

