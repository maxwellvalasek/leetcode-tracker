# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if node is None:
                return node
            print("node", node.val)
            if p.val < node.val and q.val < node.val:
                print("1")
                return dfs(node.left)
            elif p.val > node.val and q.val > node.val:
                print("2")
                return dfs(node.right)
            if p.val == node.val or q.val == node.val:
                print("3", node)
                return node
            if (p.val > node.val and q.val < node.val) or (p.val < node.val and q.val > node.val):
                print("4")
                return node
            # dfs(node.left)
            # dfs(node.right)

        return dfs(root)