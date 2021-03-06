class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = sumi = 0
        d = {0:1}
        for i in range(n):
            sumi += nums[i]
            sumj = sumi - k # 找另一半
            if sumj in d: ans += d[sumj]
            d[sumi] = d.get(sumi,0)+1 #更新dict
        return ans
