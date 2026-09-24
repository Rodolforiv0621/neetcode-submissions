class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in range(len(strs)):
            length = len(strs[i])
            string += str(length) + ";" + strs[i]
        return string
    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        res = []
        while r < len(s):
            if s[r] == ';':
            
                length = int(s[l:r])
                
                res.append(s[r+1:r+length+1])
                l = r + length+1
                
                r = r + length + 1

            else:
                r += 1
        return res