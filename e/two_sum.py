class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        pos = {}
        
        for i, x in enumerate(nums):
            if x in pos:
                pos[x].append(i)
            else:
                pos[x] = [i]
        nums.sort()
        
        while True:
            if nums[start] + nums[end] > target:
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                x1 = nums[start]
                x2 = nums[end]
                return [pos[x1][0], pos[x2][len(pos[x2])-1]]
        #44ms, 57.23%
