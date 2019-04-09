class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
          sign = -1
          x *= -1
        else:
          sign = 1;

        y = 0
        
        while x != 0:
            i = x % 10
            y *= 10
            y += i
            x //= 10
        
        y *= sign
        
        if(y > 2**31-1 or y < -2**31):
            return 0
        else:
            return y
        
        #40ms, 99.94%
