class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        minN = prices[0]
        for n in prices:
            ans = max(n - minN,ans)
            minN = min(n,minN)
        return ans