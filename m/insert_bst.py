# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        def insert(root, val):
            
            node = TreeNode(val)
            
            if not root:
                return node
            
            if not root.left and val < root.val:
                root.left = node
            elif not root.right and val > root.val:
                root.right = node
            else:
                if val > root.val:
                    insert(root.right, val)
                else:
                    insert(root.left, val)
                    
        return insert(root, val) or root 
        
        #124 ms, 74.10%
