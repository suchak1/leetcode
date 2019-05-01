class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for i in A:
            i.reverse()
            for j, y in enumerate(i):
                if y == 0:
                    i[j] = 1
                else:
                    i[j] = 0
        
        return A
        
        # 48ms, 77.63%
