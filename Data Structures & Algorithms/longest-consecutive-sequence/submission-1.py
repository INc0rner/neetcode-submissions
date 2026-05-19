class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs ={}
        maxN = 0
        for n in nums:
            hs[n] =1
        for n in nums:
            if n-1 in hs:
                continue
            else:
                maxT = 0
                for i in range(len(nums)):
                    if n+i in hs:
                        maxT += 1
                    else:
                        break
                maxN = max(maxN,maxT)
        return maxN                    

        