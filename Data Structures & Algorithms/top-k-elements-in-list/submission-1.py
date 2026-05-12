class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = {}
        for n in nums:
            if n in hs:
                hs[n] += 1
            else:
                hs[n] = 1
        
        return list(sorted(hs.keys(),key = lambda x : hs[x]))[::-1][0:k]