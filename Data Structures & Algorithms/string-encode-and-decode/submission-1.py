class Solution:

    def encode(self, strs: List[str]) -> str:
        rev = str()
        for s in strs:
            if len(str(len(s)))==1:
                range = "00"+str(len(s))
            if len(str(len(s)))==2:
                range = "0"+str(len(s))
            if len(str(len(s)))==3:
                range = str(len(s))            
            rev+= range + s
        return rev
    def decode(self, s: str) -> List[str]:
        print(s)
        rev = []
        i=0
        while i < len(s):
            wr = int(s[i]+s[i+1]+s[i+2]) #word range
            word = ""
            for k in range(i+3,i+wr+3):
                word += s[k]
            rev.append(word)
            i += wr+3
        return rev