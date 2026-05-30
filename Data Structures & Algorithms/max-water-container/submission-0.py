class Solution:
    def maxArea(self, hs: List[int]) -> int:
        l = 0
        r = len(hs) - 1
        maxN = 0
        while l <= r:
            maxN = max(maxN,(min(hs[l],hs[r])*(r-l)))
            if hs[l] < hs[r]:
                l += 1
            elif hs[l] > hs[r]:
                r -= 1
            else:
                r -= 1
        return maxN