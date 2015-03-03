"""
https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Construct Binary Tree from Preorder and Inorder Traversal  

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import TreeNode
from support import pre_order_iter, in_order_iter
from support import loads_level_order, dumps_level_order

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):   
        """ recursive version """
        def build(pre_list, in_list):
            if not pre_list or not in_list:
                return
                
            root = TreeNode(pre_list[0])
            
            root_idx = in_list.index(pre_list[0])
                       
            root.left = build(pre_list[1:root_idx+1], in_list[:root_idx])
            
            root.right = build(pre_list[root_idx+1:], in_list[root_idx+1:])
            
            return root
            
        return build(preorder, inorder)
        
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree2(self, preorder, inorder): 
        if not preorder or not inorder:
            return
        
        pre_idx, in_idx, length = 0, 0, len(preorder)
        
        root = TreeNode(preorder[0])
        pre_idx += 1
        
        node_stack = [root]
        
        while pre_idx < length:
        
            node = node_stack[-1]
            
            if inorder[in_idx] == node.val:  # no left child
                node_stack.pop()
                in_idx += 1
                if in_idx >= length:
                    break
                    
                if node_stack and inorder[in_idx] == node_stack[-1].val:
                    continue
                
                right_node = TreeNode(preorder[pre_idx])
                pre_idx += 1
                node.right = right_node
                node_stack.append(right_node)
            else:
                left_node = TreeNode(preorder[pre_idx])
                pre_idx += 1
                node.left = left_node
                node_stack.append(left_node)

        return root
        
        
def test_main():
    sol = Solution()

    def test(str_tree):
        print("\nload str tree:")
        print(str_tree)
        tree_root = loads_level_order(str_tree)
        print("dump str tree:")
        print(dumps_level_order(tree_root))
                
        preorder = [n.val for n,d in pre_order_iter(tree_root)]
        print("preorder:", preorder)
        inorder = [n.val for n,d in in_order_iter(tree_root)]
        print("inorder:", inorder)
        
        print("new tree: ", dumps_level_order(sol.buildTree(preorder, inorder)))
        print("new tree2: ", dumps_level_order(sol.buildTree2(preorder, inorder)))
    
    trees = [
        "{1,2,3,4,5,6,7,8,9,10,11,12,13,14}",
        "{3,9,20,#,#,15,7}",
        "{1,2,3,#,#,4,#,#,5}",
        "{1,2,2,3,4,4,3}",
        "{1,2,2,#,3,#,3}",
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
