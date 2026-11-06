class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        if len(arr) == 1:
            return [-1]

        for i in range(len(arr)-1):
            maxNum = float('-inf');
            for j in range(i+1,len(arr)):
                maxNum = max(maxNum, arr[j])
            arr[i] = maxNum

        arr[-1] = -1
        return arr