class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left = 0
        right = len(S)
        result = []
        
        for i in S:
            if i == "D":
                result.append(right)
                right -= 1
            else:
                result.append(left)
                left += 1

        result.append(left)
        return result
        
        #88ms, 73.54%
