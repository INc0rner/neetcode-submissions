class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for i,n in enumerate(nums):
            if n in hs:
                return [hs[n],i]
            else:
                hs[target - n] = i