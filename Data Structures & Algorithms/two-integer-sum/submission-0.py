class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mySet = set()
        for index, i in enumerate(nums):
            if target-i in mySet:
                for index2, j in enumerate(nums):
                    if j == target-i:
                        return [index2, index]
            mySet.add(i)