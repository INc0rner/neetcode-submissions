class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        allp = 1 # all product
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
                continue
            else:
                allp *= n
        rev = []
        for n in nums:
            if zero_count > 0:
                if n == 0 and zero_count == 1:
                    rev.append(allp)
                else:
                    rev.append(0)
            else:
                rev.append(allp//n)
        return rev