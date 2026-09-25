class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countsA = {}
        countsB = {}
        for i in range(len(s)):
            countsA[s[i]] = countsA.get(s[i], 0) + 1
            countsB[t[i]] = countsB.get(t[i], 0) + 1
        
        return countsA == countsB

