class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        per = {}
        check = {}
        l = 0
        for c in set(s1):
            check[c] = s1.count(c)

        for r in range(len(s2)):
            # print(s2[l],s2[r],check)
            if s2[r] in check:
                check[s2[r]] -= 1

            if r-l+1 > len(s1):
                if s2[l] in check:
                    check[s2[l]] += 1
                l += 1

            if r-l+1 == len(s1) and all(v == 0 for v in check.values()):  
                return True 

            # print(l,s2[l],r,s2[r],check,"\n")       
        return False

                