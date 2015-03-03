"""
https://oj.leetcode.com/problems/same-tree/

Same Tree

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are 
structurally identical and the nodes have the same value.
"""

from support import loads_level_order, dumps_level_order

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):           
        stack = [(p, q)]
    
        while stack:
            node1, node2 = stack.pop()
            
            if node1 is None or node2 is None:
                if node1 is None and node2 is None:
                    continue
                else:
                    return False
            
            if node1.val != node2.val:
                return False
                       
            stack.append((node1.right, node2.right))
                
            stack.append((node1.left, node2.left))
                
        return True
        
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree2(self, p, q):
        if p is None or q is None:
            return p is None and q is None
        elif p.val == q.val:
            return self.isSameTree2(p.left, q.left) and self.isSameTree2(p.right, q.right)
        else:
            return False
            
        
def test_main():
    import random
    sol = Solution()

    def test(s1, s2):
        print("\nload str tree:")
        print(s1, s2)
        t1, t2 = loads_level_order(s1),  loads_level_order(s2)
        print("dump str tree:")
        print(dumps_level_order(t1), dumps_level_order(t2))
                                     
        print("answer: %s %s" % (sol.isSameTree(t1, t2), sol.isSameTree2(t1, t2)))
    
    trees = [
        ("{1,2,3,4,5,6,7,8,9,10,11,12,13,14}","{1,2,3,4,5,6,7,8,9,10,11,12,13,14}"),
        ("{3,9,20,#,#,15,7}", ""),
        ("{1,2,3,#,#,4,#,#,5}", "{1,2,3,#,#,5,#,#,5}"),
        ("{1,2,2,3,4,4,3}", "{1,2,2,3,4,4,3}"),
        ("{1,2,2,#,3,#,3}", "{1,2,2,#,3,#,3}"),
        ("{1,2,2,3,#,#,3}", "{1,2,2,3,#,#,3}"),
        ("{1,2}", ""),
        ("{1,#,2}", ""),
        ("{1,2,3}", "{1,2}"),
        ("{1,#,2,3}", "{1,#,2,3}"),
        ("{#}", "{}"),
        ("{1}", "{2}"),
        ("{}", "{}"),
        (str(range(20)), str(range(20))),
        ("{1,#,2,3}", "{1,#,2,3}"),
        ("{1,#,2,#,3}", "{1,#,2,#,3}"),
        ("{1,#,2,#,3,#,4,#,5,#,6,#,7,#,8}", "{1,2,#,3,#,4,#,5,#,6,#,7,#,8}"),
    ]

    for s1,s2 in trees:
        test(s1, s2)
        
if __name__ == "__main__":
    test_main()
