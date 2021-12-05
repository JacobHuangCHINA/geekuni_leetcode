class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ''
        for ch in s:
            print(res)
            res += ch.lower()
        return res