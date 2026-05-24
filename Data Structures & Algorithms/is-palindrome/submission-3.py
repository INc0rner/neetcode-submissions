import string
class Solution:
    def isPalindrome(self, a: str) -> bool:
        s = a.lower()
        d = string.ascii_letters + "1234567890"
        r = 0
        l = len(a) - 1
        while r <= l:
            print(r,l)
            while s[r] not in d and r < l:
                r += 1
            while s[l] not in d and r < l:
                l -= 1
            if s[r] != s[l]:
                return False
            else:
                r += 1
                l -= 1
        return True