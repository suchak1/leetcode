class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = {}
        
        for i, x in enumerate(nums):
            if x in pos:
                pos[x].append(i)
            else:
                pos[x] = [i]
        
        for x in pos.keys():
            if target-x in pos:
                if target-x == x:
                    if len(pos[x]) == 2:
                        return [pos[x][0], pos[x][1]]
                    else:
                        continue
                else:
                    return [pos[x][0], pos[target-x][0]]
                #40ms, 86.10%
