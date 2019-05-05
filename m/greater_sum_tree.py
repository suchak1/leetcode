# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def collectSum(self, root):
        if not roaot:
            return [0]
        else:
            return [root.val] + self.collectSum(root.left) + self.collectSum(root.right)
    
    def replaceVal(self, root, sumList):
        if not root:
            return
        else:
            root.val = sum([i if i >= root.val else 0 for i in sumList])
            self.replaceVal(root.left, sumList)
            self.replaceVal(root.right, sumList)
        
        
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sumList = self.collectSum(root)
        self.replaceVal(root, sumList)
        return root
        
        #60 ms, 100.00%
