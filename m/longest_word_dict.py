class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        lookup = {word:1 for word in words}
        maxWord = ""
        
        for word in words:
            if len(word) < len(maxWord):
                continue 
                
            prefix = ""
            
            for x in word:
                prefix += x
                if prefix == word:
                    if len(word) > len(maxWord) or (len(word) == len(maxWord) and word < maxWord):
                        maxWord = word
                elif prefix not in lookup:
                    break
            
        return maxWord
            
        # 96ms, 47.58%
