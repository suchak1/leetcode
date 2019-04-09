class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = {}
        tot = 0
        
        for i in S:
            d[i] = d.get(i, 0) + 1

        
        for i in J:
            tot += d.get(i, 0)
        
        return tot
        
        #36ms, 99.66%
        
