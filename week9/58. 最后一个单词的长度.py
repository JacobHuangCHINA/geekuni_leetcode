class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split(' ')
        return len([ch for ch in temp if ch][-1])