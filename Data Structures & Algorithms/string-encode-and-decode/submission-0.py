class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            encoded += str(len(word)) + ";" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            length = ''
            while s[i] != ';':
                length += s[i]
                i+=1
            length = int(length)
            word = ''
            i += 1
            for j in range(length):
                word += s[i]
                i += 1
            ans.append(word)
        return ans
            
        