# -*- coding: utf-8 -*-
"""
Leetcode OJ support lib of linked list

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
         
    def __iter__(self):
        _node = self
        while _node:
            yield _node
            _node = _node.next
            
        raise StopIteration
            
    def __str__(self):
        return "<Node> %s" % self.val
        
    __repr__ = __str__

    @classmethod
    def create_list(cls, count=-1, start=0, items=None):
        if count <= 0 and not items:
            return []
        
        if items:
            head = cls(items[start])
        else:
            head = cls(start)
            
        cur_node = head
        
        if count < 0:
            count = len(items) - 1
        
        for i in xrange(start+1, count+1):
            val = i if not items else items[i]
            new_node = cls(val)
            cur_node.next = new_node
            cur_node = new_node

        return head
        

class DoublyLinkedNode(object):
    """
    Doubly-Linked and Circular Lists Node
    """
    __slots__ = ("prev", "next", "value")

    def __init__(self, prev=None, next=None, value=None):
        self.prev = prev
        self.next = next
        self.value = value

    def __repr__(self):
        return "%08X <- %08X -> %08X [Value: %s]" % (id(self.prev), id(self), id(self.next), self.value)

    def __iter__(self):
        node = self
        yield node
        while node.next is not None and node.next != self:
            node = node.next
            yield node

    def __reversed__(self):
        node = self
        yield node
        while node.prev is not None and node.prev != self:
            node = node.prev
            yield node


class DoublyLinkedList(object):
    """
    Doubly-Linked and Circular List
    http://www.brpreiss.com/books/opus7/html/page165.html
    http://code.activestate.com/recipes/576693/
    """
    def __init__(self):
        self._head = head = DoublyLinkedNode(None, None, None)
        head.prev, head.next = head, head
        self._count = 0

    def append(self, node):
        head = self._head
        node.prev, node.next = self._head.prev, head

        head.prev.next = node
        head.prev = node
        self._count += 1

    push = append

    def appendleft(self, node):
        head = self._head
        node.prev, node.next = head, head.next

        head.next.prev = node
        head.next = node
        self._count += 1

    pushleft = appendleft

    def clear(self):
        self._head = head = DoublyLinkedNode(None, None, None)
        head.prev, head.next = head, head
        self._count = 0

    def count(self):
        return self._count

    def pop(self):
        node = self._head.prev
        node_prev = node.prev
        self._head.prev = node_prev
        node_prev.next = self._head
        self._count -= 1
        return node

    def popleft(self):
        node = self._head.next
        node_next = node.next
        self._head.next = node_next
        node_next.prev = self._head
        self._count -= 1
        return node

    def remove(self, node):
        if node.next is not None:
            node.next.prev, node.prev.next = node.prev, node.next
            self._count -= 1
        return node

    def __iter__(self):
        for n in self._head:
            yield n

    def __reversed__(self):
        for n in reversed(self._head):
            yield n
