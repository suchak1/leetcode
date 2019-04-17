# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> 'TreeNode':
        if not len(nums):
            return None

        val = max(nums)
        node = TreeNode(val)

        if len(nums) == 1:
            return node

        pos = nums.index(val)

        left = nums[:pos]
        right = nums[pos+1:]


        node.left = self.constructMaximumBinaryTree(left)
        node.right = self.constructMaximumBinaryTree(right)

        return node
        
        #144ms, 85.31%
