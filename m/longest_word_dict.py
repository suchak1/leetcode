class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        lookup = {word:1 for word in words}
        maxWord = ""
        
        for y, word in enumerate(words):
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
            
        # 100ms, 46.38%
