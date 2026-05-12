class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = {}
        for word in strs:
            s = "".join(sorted(word))
            if s in hs:
                hs[s].append(word)
            else:
                hs[s] = [word]
        return list(hs.values())
            
