class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        ans = [0] * len(arr)
        maxNum = float('-inf');
        for i in range(len(arr)-1,-1, -1):
            if i == len(arr)-1:
                ans[i] = -1
            else:
                maxNum = max(maxNum, arr[i+1]);
                ans[i] = maxNum

        return ans
            

        #[ 18 , 6 , 6 , 6 , 1, -1] 