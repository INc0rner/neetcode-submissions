class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def deal(s):
            l = s.split(",")
            return [int(l[0]),int(l[1]),int(l[2])]
        nums = sorted(nums)
        rev = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r and l != i and r != i:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] == 0:
                    rev.add(str(nums[i]) +","+ str(nums[l])+","+ str(nums[r]))
                    l += 1
                    r -= 1
        # print()
        return list(map(deal,rev))