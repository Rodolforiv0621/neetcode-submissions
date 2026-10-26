class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
            
        stack = []
        fullSet = {'}': '{', ')': '(', ']': '['}
        
        for char in s:
            if char not in fullSet:
                stack.append(char)
            else:
                if not stack or stack.pop() != fullSet[char]:
                    return False
                
        return not stack

