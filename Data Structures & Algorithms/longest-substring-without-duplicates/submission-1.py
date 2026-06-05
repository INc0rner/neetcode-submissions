class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        for i in range(n,0,-1):
            for j in range(n-i+1):
                if len(s[j:j+i]) == len(set(s[j:j+i])):
                    return i
        return 0