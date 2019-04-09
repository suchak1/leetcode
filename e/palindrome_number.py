class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        return str(x) == str(x)[::-1]

        #80ms, 97.43%
