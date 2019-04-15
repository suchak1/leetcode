class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = 0
        last = []


        for op in ops:
            #print(score, last)
            if op == "+":
                score += sum(last[-2:])
                last.append(sum(last[-2:]))
            elif op == "D":
                score += last[-1] * 2
                last.append(last[-1] * 2)
            elif op == "C":
                score -= last[-1]
                last.pop()
            else:
                score += int(op)
                last.append(int(op))
        
        return score
                
        #40ms, 61.07%
