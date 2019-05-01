"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def depth(self, node, count):
        if not node:
            return count
        else:
            search = [self.depth(child, count + 1) for child in node.children]
            return max(search) if search else count + 1
    
    def maxDepth(self, root: 'Node') -> int:
        return self.depth(root, 0)
        
        # 92ms, 48.20%
