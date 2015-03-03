"""
https://oj.leetcode.com/problems/symmetric-tree/

Symmetric Tree  

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details. 
"""

from support import level_order_iter
from support import loads_level_order, dumps_level_order 

    
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        """ recursively version """
        if root is None:
            return True
            
        def check_node(left, right):
            if left is None and right is None:
                return True 
                
            if left is None or right is None:
                return False
                
            if left.val != right.val:
                return False
                
            return check_node(left.left, right.right) and check_node(left.right, right.left)
        
        return check_node(root, root)
        
    def isSymmetric1(self, root):
        """ iteratively version using stack  """
        if root is None:
            return True
            
        waiting_stack = [(root.left, root.right)]
        
        while waiting_stack:
            left, right = waiting_stack.pop()
            
            if left is None and right is None:
                continue
            
            if left is None or right is None:
                return False
            
            if left.val != right.val:
                return False
            
            waiting_stack.append((left.left, right.right))
            waiting_stack.append((left.right, right.left))
            
        return True
        
    def isSymmetric2(self, root):
        """ iteratively version with level order iter """
        if root is None:
            return True
            
        if root.left is None and root.right is None:
            return True
                          
        def check_cur_level(nodes):
            if len(nodes) <= 1:
                return True
                
            for i in xrange(len(nodes)/2):
                if nodes[i] != nodes[-i-1]:
                    return False
            
            return True
           
        # Start symmetric check
        res = []         
        cur_level = 0
        for node, depth in level_order_iter(root, True):
            if depth == cur_level:
                if node is None:
                    res.append("#")
                else:
                    res.append(node.val)
            else:
                if check_cur_level(res) is False:
                    return False
                res = []
                cur_level += 1
                
                if node is None:
                    res.append("#")
                else:
                    res.append(node.val)
                                
        return check_cur_level(res)
 
 
def test_main():
    sol = Solution()

    def test(str_tree):
        print("\nload str tree:")
        print(str_tree)
        tree_root = loads_level_order(str_tree)
        print("dump str tree:")
        print(dumps_level_order(tree_root))
                
        print("is symmetric: %s" % sol.isSymmetric(tree_root))
        print("is symmetric: %s" % sol.isSymmetric1(tree_root))
        print("is symmetric: %s" % sol.isSymmetric2(tree_root))
    
    trees = [
        "{1,2,3,4,5,6,7,8,9,10,11,12,13,14}",
        "{3,9,20,#,#,15,7}",
        "{1,2,3,#,#,4,#,#,5}",
        "{1,2,2,3,4,4,3}",
        "{1,2,3,#,#,4,#,#,5}",
        "{1,2,2,#,3,#,3}",
        "{1,2,2,3,#,#,3}",
        "{1,2}",
        "{1,#,2}",
        "{1,#,2,3}",
        "{#}",
        "{1}",
        "{}",
        "{1,2,2,#,3,#,3,#,#,4,#}",
        "{1,2,2,3,#,#,3,#,4,4,#}",
        "{1,2,2,3,#,#,3,4,#,#,#,#,#,#,4}",
        "{1,2,2,3,#,#,3,4,#,#,4,5,#,#,5}"
    ]

    for s in trees:
        test(s)
    
if __name__ == "__main__":
    test_main()
