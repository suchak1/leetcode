class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        if S == "":
            return S
        
        lcount = 0
        rcount = 0
        final = ""
        start = 0
        
        for i, x in enumerate(S):
            if x == "(":
                lcount += 1
            else:
                rcount += 1
            
            if lcount == rcount:
                final += S[start+1:i]
                start = i+1
                lcount = 0
                rcount = 0
                
        return final
            
        #44ms, 94.26%
        
        
        
            
        
        
                
                
