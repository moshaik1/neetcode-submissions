class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = []
        hashTable = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hashTable:
                hashTable[sorted_word] = [word]
            else:
                hashTable[sorted_word].append(word)
        
        for vals in hashTable.values():
            ans.append(vals)

        return ans
strs=["act","pots","tops","cat","stop","hat"]


# strs=["pots","act","tops","cat","stop","hat"]
# [ 'opst'  ]