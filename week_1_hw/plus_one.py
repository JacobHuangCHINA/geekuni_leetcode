class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        for i in range(len(digits)-1, -1 ,-1):
            digits[i] += 1 
            digits[i] %= 10 
            if digits[i] != 0: return digits
        digits = [1] + digits[:]
        return digits

