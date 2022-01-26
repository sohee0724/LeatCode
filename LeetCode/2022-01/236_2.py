# Definition for a binary tree node.

from inspect import stack


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left:
            return right
        if not right:
            return left
        
        return root
        
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root:None}
        
        while p not in parent or q not in parent:
            node = stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node 
                stack.append(node.right)
                
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
            
        return q