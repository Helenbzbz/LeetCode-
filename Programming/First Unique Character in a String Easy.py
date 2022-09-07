## Use collections.Counter to calculate the count => and then uses enumerate and if count[ch] == 1: return idx

## This will not work if too long string
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = list(s)
        for i in range(0, len(s)):
            check = char_dict.copy()
            check.pop(i)
            if char_dict[i] not in check: 
                return i
        return -1
    
## Let's do another one with hashmap
## We have a collection of counts by words, each word will have a frequency stored as a dictionary; we then loop through idex and word, if any word frequency > 1, return index
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1
