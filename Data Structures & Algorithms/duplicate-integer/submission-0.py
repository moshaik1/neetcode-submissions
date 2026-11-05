
#
# return True if Duplicates
# return False if unique values
# iterate once and add to Hash set?
# 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numSet = set()

        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                return True
        return False
        