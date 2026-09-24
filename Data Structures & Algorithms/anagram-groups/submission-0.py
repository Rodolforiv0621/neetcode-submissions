class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)
        for stri in strs:
            arr = [0] * 26
            for char in stri:
                arr[ord(char) - ord('a')] += 1
            hashmap[tuple(arr)].append(stri)
        return list(hashmap.values())
            