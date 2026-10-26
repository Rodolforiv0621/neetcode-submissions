class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        q = []
        closeSet = [')', '}', ']']
        fullSet = ['()', '{}', '[]']
        for char in s:
            if char not in closeSet:
                q.append(char)
            elif char in closeSet:
                if not q or q[-1] + char not in fullSet:
                    return False
                q.pop()

        if len(q) == 0:
            return True
        else:
            return False

