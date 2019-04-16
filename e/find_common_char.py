class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        lookup = {}
        
        for letter in A[0]:
            lookup[letter] = lookup.get(letter, 0) + 1
        
        def findCommon(lookup, word):
            common = {}
            
            for i in word:
                if i in lookup:
                    common[i] = common.get(i, 0) + 1
                    if lookup[i] == 1:
                        del lookup[i]
                    else:
                        lookup[i] -= 1
            return common
        
        for word in A[1:]:
            lookup = findCommon(lookup, word)
        
        common = [[i]*lookup[i] for i in lookup.keys()]
        common = [item for sublist in common for item in sublist]
        
        return common
        
        #52ms, 90.79%
