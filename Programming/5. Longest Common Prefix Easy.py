## Intuition is to search throug all the strings through iteration
## We use search of the first 2 strings and the latter 2 strings and combine their results
## Prefix!!! It always start from the beginning

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0: 
            return prefix
        
        for i in range(len(min(strs))):
            ## The longest prefix won't exceed the shortest str
            c = strs[0][i]
            if all(a[i] == c for a in strs):
            ## all will return true if the condition met in all the iterations
                prefix+=c
            else:
                break
        return prefix
