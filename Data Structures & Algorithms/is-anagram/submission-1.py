class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False
        else:
            ansDict = {}

            for char in s:
                if char not in ansDict:
                    ansDict[char] = 1
                else:
                    ansDict[char] += 1
            for char in t:
                if char not in ansDict:
                    return False
                else:
                    ansDict[char] -= 1
                
            for value in ansDict.values():
                if value != 0:
                    return False
            return True