class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        start = 0
        end = 1
        longest = 1
        
        for i, n in enumerate(nums):
            if nums[i-1] < n:
                end = i + 1
            else:
                start = i
            
            if end-start > longest:
                    longest = end-start
        return longest
    
        # 44ms, 89.25%
