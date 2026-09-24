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
            j = i
            while s[j] != ';':
                j += 1
            print(s[i:j])
            length = int(s[i:j])
            i = j + 1
            j += length +1
            word = s[i:j]
            ans.append(word)
            i = j
        return ans

    
            
        