class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1
        
        for i in range(len(t)):
            hashmap[t[i]] = hashmap.get(t[i], 0) - 1
        
        for value in hashmap.values():
            if value != 0:
                return False
        return True