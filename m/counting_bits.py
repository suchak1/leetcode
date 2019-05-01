class Solution:
    def countBits(self, num: int) -> List[int]:
        return [bin(i).count("1") for i in range(0, num + 1)]
        # 120ms, 52.90%
