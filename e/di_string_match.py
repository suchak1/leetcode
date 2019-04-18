class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        nums = list(range(len(S)+1))
        
        result = [nums.pop() if letter == "D" else nums.pop(0) for letter in S]

        if len(nums):
            result.append(nums.pop())
     
        return result
        #104ms, 29.92%
