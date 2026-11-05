class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict = {}

        for char in s:
            if char not in dict:
                dict[char] = 1
            else: 
                dict[char] += 1

        for char in t:
            if char not in dict:
                return False
            else:
                dict[char] -= 1

        for value in dict.values():
            if value != 0:
                return False
        return True