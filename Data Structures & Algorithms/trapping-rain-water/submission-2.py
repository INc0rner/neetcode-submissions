class Solution:
    def trap(self, hts: List[int]) -> int:
        lht = []
        pos = 0
        for n in hts:
            pos = max(pos,n)
            lht.append(pos)
        rht = [0 for _ in range(len(hts))]
        pos = 0
        for i in range(len(hts)):
            pos = max(pos,hts[-i-1])
            rht[-i-1] = pos
        ans = 0
        print(lht)
        print(rht)
        for i in range(len(hts)):
            ans += max((min(lht[i],rht[i]) - hts[i]),0)
        return ans
