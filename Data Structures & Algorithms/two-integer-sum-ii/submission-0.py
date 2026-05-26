class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l +=1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                rev = [l+1,r+1]
                return rev
