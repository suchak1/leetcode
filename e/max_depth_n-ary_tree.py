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
            maxDepth = count + 1
            for child in node.children:
                currDepth = self.depth(child, count + 1)
                if currDepth > maxDepth:
                    maxDepth = currDepth
            
            return maxDepth
    
    def maxDepth(self, root: 'Node') -> int:
        return self.depth(root, 0)

        #88ms, 79.99%
