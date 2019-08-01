class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()[::-1]
        return " ".join(words).strip()
        
        # 32ms, 93.37%
