class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort()
        maxWord = ""
        lookup = {}
        
        for word in words:
            lookup[word] = 1
            
            if len(word) < len(maxWord):
                continue
                
            prefix = ""
            
            for i, x in enumerate(word):
                prefix += x
                if i == len(word) - 1:
                    if len(word) > len(maxWord):
                        maxWord = word
                    break
                if prefix in lookup:
                    continue
                else:
                    break
            
        return maxWord
            
        # 132ms, 30.07%
