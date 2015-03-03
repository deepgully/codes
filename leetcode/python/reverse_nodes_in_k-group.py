"""
https://oj.leetcode.com/problems/reverse-nodes-in-k-group/

Reverse Nodes in k-Group 

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

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
    def node_group_iter(self, node, k):
        li =[]
        while node:
            saved_next = node.next
            
            li.append(node)                
            if len(li) == k:
                li.reverse()
                for n in li:
                    yield n
                li = []
                
            node = saved_next
        else:
            for n in li:
                yield n
            
        raise StopIteration
            
    def reverseKGroup(self, head, k):   
        if head is None:
            return None
            
        if k <= 1:
            return head
                        
        new_head = ListNode(-1)
        
        pre_node = new_head
               
        for node in self.node_group_iter(head, k):
            pre_node.next = node
            pre_node = node

        pre_node.next = None

        return new_head.next
            
    def reverseKGroup1(self, head, k):   
        if head is None:
            return None
            
        if k <= 1:
            return head
            
        cur_node = head
        length = 0
        while cur_node:
            cur_node = cur_node.next
            length += 1
            
        if k > length:
            return head
            
        index = 1 
        root_node = ListNode(-1)
        root_node.next = head
        
        pre_node = root_node
        cur_node = head
        
        
        saved_head = root_node
        saved_head_next = head
        
        while cur_node:
            if (length - index) < (length % k):
                break
                
            print(index, "cur_node", cur_node)
        
            saved_next = cur_node.next
            cur_node.next = pre_node
            
            if (index % k) == 0:
                saved_head.next = cur_node
                saved_head_next.next = saved_next
                saved_head = saved_head_next
                pre_node = saved_head
                saved_head_next = saved_next
            else:
                pre_node = cur_node
            
            cur_node = saved_next
            index += 1
            
        return root_node.next


def test_main(passes=10):
    import random
    sol = Solution()
    
    for i in xrange(passes):
        input = ListNode.create_list(i)

        k = random.randint(0, i/2)

        print("\n reverse %s in %s" % (k, input and list(input)))
        new_node = sol.reverseKGroup(input, k)

        print("answer:")
        print(new_node and list(new_node))

if __name__ == "__main__":
    test_main()              
   


        