# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def unival(self, root, val):
        if not root:
            return True
        else:
            return root.val == val and self.unival(root.left, val) and self.unival(root.right, val)
        
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.unival(root, root.val) 
        #36ms, 91.69%
