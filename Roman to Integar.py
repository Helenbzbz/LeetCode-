# My intuition thought was to count from left to right
# but then realized by counting from right to the left, we can do less comparison and also less index reference
  
val_dict = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000  
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = val_dict.get(s[-1])
        for i in reversed(range(len(s)-1)):
            cv = val_dict.get(s[i])
            rv = val_dict.get(s[i+1])
            if cv < rv:
                total -= cv
            else:  
                total += cv
        return total
