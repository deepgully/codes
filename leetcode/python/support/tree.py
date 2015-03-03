# -*- coding: utf-8 -*-
"""
Leetcode OJ support lib of tree

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""

import collections


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        
    def __repr__(self):
        return "<Node %s>" % self.val
        
    __str__ = __repr__
    
    def __iter__(self):
        return in_order_iter(self)
    

def print_node(node, depth=None):
    print(depth, node)
    
    
def get_depth(node):
    if not node:
        return 0
    left = get_depth(node.left)
    right = get_depth(node.right)
    return max(left, right) + 1

    
def in_order_traversal(root, callback=None, cur_depth=0):
    if root is None:
        return
    
    in_order_traversal(root.left, callback, cur_depth+1)
    callback and callback(root, cur_depth)
    in_order_traversal(root.right, callback, cur_depth+1)
       
            
def in_order_iter(root, cur_depth=0):
    if root is None:
        raise StopIteration
    
    stack = []
    node = root
    
    level = 0
    while node is not None:
        stack.append((node, (cur_depth + level)))
        node = node.left
        level += 1
        
    while stack:
        node, cur_depth = stack.pop()
        
        yield node, cur_depth
        
        node = node.right
        cur_depth += 1
        
        level = 0
        while node is not None:
            stack.append((node, (cur_depth + level)))
            node = node.left
            level += 1
            
            
def pre_order_traversal(root, callback=None, cur_depth=0):
    if root is None:
        return
    
    callback and callback(root, cur_depth)
    pre_order_traversal(root.left, callback, cur_depth+1)
    pre_order_traversal(root.right, callback, cur_depth+1)
    

def pre_order_iter(root, cur_depth=0):
    if root is None:
        raise StopIteration
    
    stack = [(root, cur_depth)]
    
    while stack:
        node, cur_depth = stack.pop()
        
        yield node, cur_depth
        
        if node.right is not None:
            stack.append((node.right, (cur_depth + 1)))
            
        if node.left is not None:
            stack.append((node.left, (cur_depth + 1)))
            

def post_order_traversal(root, callback=None, cur_depth=0):
    if root is None:
        return
    
    post_order_traversal(root.left, callback, cur_depth+1)
    post_order_traversal(root.right, callback, cur_depth+1)
    callback and callback(root, cur_depth)
    
    
def post_order_iter(root, cur_depth=0):
    if root is None:
        raise StopIteration
        
    parents = []
    last_visted = None
    node = root
    
    while parents or node is not None:
        if node is not None:
            parents.append((node, cur_depth))
            node = node.left
            cur_depth += 1
        else:
            top_node, cur_depth = parents[-1]
            if top_node.right is not None and last_visted != top_node.right:
                node = top_node.right
                cur_depth += 1
            else:
                yield top_node, cur_depth
                last_visted, cur_depth = parents.pop()       
                
        
def level_order_traversal(root, callback=None, completed_tree=False):
    if root is None:
        return
    
    current_level = [root]
    cur_depth = 0
    while current_level:
        next_level = []
        all_done = True
        
        for node in current_level:
            callback and callback(node, cur_depth)
                
            if node is not None: 
            
                if completed_tree:
                    next_level.append(node.left)
                    next_level.append(node.right)
                    if node.left is not None or node.right is not None:
                        all_done = False
                else:  
                    if node.left is not None:
                        all_done = False
                        next_level.append(node.left)
                        
                    if node.right is not None:
                        all_done = False
                        next_level.append(node.right)
                        
        if all_done:
            break
                
        current_level = next_level
        cur_depth += 1
    
    
def level_order_iter(root, completed_tree=False):
    if root is None:
        raise StopIteration
        
    current_level = [root]
    cur_depth = 0
    while current_level:
        next_level = []
        all_done = True
        
        for node in current_level:
            yield (node, cur_depth)
            if node is not None:    
                if completed_tree:
                    next_level.append(node.left)
                    next_level.append(node.right)
                        
                    if node.left is not None or node.right is not None:
                        all_done = False
                        
                else:
                    if node.left is not None:
                        all_done = False
                        next_level.append(node.left)
                    if node.right is not None:
                        all_done = False
                        next_level.append(node.right)
                            
        if all_done:
            raise StopIteration
            
        current_level = next_level
        cur_depth += 1
    

def create_node(str_node):
    if str_node == "#":
        return None
    
    return TreeNode(int(str_node))

    
def loads_level_order(str_tree):
    str_nodes = [s.strip() for s in str_tree.strip(" {}[]()").split(",") if s and s.strip()] 
    
    length = len(str_nodes)
    
    if length == 0:
        return None
        
    root = create_node(str_nodes[0])
       
    index = 1
   
    parents = collections.deque([root])
    
    while index < length: 
        if len(parents) == 0:
            break
            
        cur_parent = parents.popleft()
        if cur_parent is None:
            continue
            
        left_node = create_node(str_nodes[index])
        cur_parent.left = left_node
               
        index += 1
        
        if index >= length:
            break
            
        right_node = create_node(str_nodes[index])
        cur_parent.right = right_node
        
        index += 1
        
        parents.append(left_node)
        parents.append(right_node)
    
    return root
    
    
def dumps_level_order(root, order="level"):
    output = []
    def dump_node(node, cur_depth):  
        if node is None:
            output.append("#")
        else:
            output.append(str(node.val))
    
    level_order_traversal(root, dump_node, completed_tree=True)
        
    output = ",".join(output).rstrip("#,")
    
    return "{%s}" % output
    
    
def bst_insert(node, value, allow_dup=False):   
    if node is None:
        return TreeNode(value)
        
    if not allow_dup and value == node.val:
        return node
        
    if value <= node.val:
        node.left = bst_insert(node.left, value, allow_dup)
    else:
        node.right = bst_insert(node.right, value, allow_dup)
        
    return node
                
        
def bst_create(values):
    tree = None
    for v in values:
        tree = bst_insert(tree, v)
    return tree
