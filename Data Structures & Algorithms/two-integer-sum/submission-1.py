# given array of ints:nums and int:target
# return i and j such that nums[i] and nums[j] == target
# i != j

# Questions 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        numsLen = len(nums)

        for i in range(0, numsLen-1):
            for j in range(i+1, numsLen):
                sumVal = nums[i]+nums[j]
                if sumVal == target:
                    ans.append(i)
                    ans.append(j)
                    return ans; 
                
        return ans;     



