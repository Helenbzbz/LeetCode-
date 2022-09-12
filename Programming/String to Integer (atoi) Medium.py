class Solution:
    def myAtoi(self, s: str) -> int:
        negative_sign = 1
        n = 0
        if not s: return 0
        if s[n] == ' ':
            while s[n] == ' ':
                if n == len(s) -1: return 0
                n+=1
        
        if s[n] in ['-','+']:
            if n == len(s) -1: return 0
            if s[n] == '-': negative_sign = -1
            n+=1
        
        result = []
        while n < len(s) and s[n].isnumeric():
            result.append(s[n])
            n+=1
            
        if result == []: return 0
        num = int(''.join(result))*negative_sign
        if num < -2**31:
            return (2**31)*negative_sign
        if num >= 2**31: return 2**31-1
        
        return num
