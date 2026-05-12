class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = {}
        def combi(l):
            s = ""
            for c in l:
                s += c
            return s
        for word in strs:
            s = combi(sorted(word))
            if s in hs:
                hs[s].append(word)
            else:
                hs[s] = [word]
        return list(hs.values())
            
