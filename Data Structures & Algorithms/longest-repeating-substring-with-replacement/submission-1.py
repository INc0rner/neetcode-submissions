class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        saw = {}
        l = 0
        ans = 1
        for r in range(len(s)):
            if s[r] in saw:
                saw[s[r]] += 1
            else:
                saw[s[r]] = 1
            while (r - l + 1) - max(saw.values()) > k:
                saw[s[l]] -= 1
                l += 1
            ans = max(ans,(r-l+1))
        return ans
            

