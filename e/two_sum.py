class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        pos = {}
        
        for i, x in enumerate(nums):
            if target-x in pos:
                return [i, pos[target-x][0]]
            else:
                pos[x] = [i]
        #40ms, 86.10%
