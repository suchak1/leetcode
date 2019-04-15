class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = "QWERTYUIOP"
        first += first.lower()
        second = "ASDFGHJKL"
        second += second.lower()
        #third = "ZXCVBNM"
        #third += third.lower()
        
        lookup1 = {i:1 for i in first}
        lookup2 = {i:2 for i in second}
        #lookup3 = {i:3 for i in third}
        
        result = []
        
        def findRow(letter, lookup1, lookup2):
            if letter in lookup1:
                return 1
            elif letter in lookup2:
                return 2
            else:
                return 3
        
        for word in words:
            if word == "":
                continue
            
            rowNum = findRow(word[0], lookup1, lookup2)
            keep = 1
            
            for letter in word:
                if findRow(letter, lookup1, lookup2) != rowNum:
                    keep = 0
                    break
            
            if keep:
                result.append(word)
                
        return result
        #36ms, 73.72%
