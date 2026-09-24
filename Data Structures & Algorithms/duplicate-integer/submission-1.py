class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        thisSet = set()
        for i in nums:
            if i in thisSet:
                return True
            else:
                thisSet.add(i)
        return False