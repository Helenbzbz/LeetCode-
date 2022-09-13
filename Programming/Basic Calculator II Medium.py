## Logic is to scan from left to right and run through the following logics
## 1. if charactor is 0~9, add to current number
## 2. current charactor otherise has to be operation (+,-,*,/), evaluate expression based on operation
## 3. +/-, evaluate based on next operation -> must store current number -> push current number to Stack; * or / pop top values and push back

class Solution:
    def calculate(self, s: str) -> int:
        p = 0
        n_s = 0
        sign = 1
        num = 0 # num: store the current number we run through
        op = "+"
        
        mp = {'+':1, '-':-1}
        
        s += '+'
        # We loop through the char in s
        for c in s:
        # if char is a number, then we add the char to current num
            if c.isnumeric():num = num*10 + int(c)
        # if char is an oepration, we will see if it's add-minus or multiply-divide operations
        # if it is * or /, we take previous to time the current or divide
            elif c in "+-*/":
                if op in '*/':
                    if op == '*': num = p*num
                    else: num = floor(p/num)
        # The sign is orignally +, and then n_s is current number * sign -> change sign but not until the next time we meet a +/- we can't conclude this number -> there might be */ in between we have to keep searching for it until we meet another +/-!!! That is why we append an add at the end to trigger the last calculation
                if c in '+-': 
                    n_s += sign*num
                    sign = mp[c]
                else:p = num
                op = c
                num = 0
        return floor(n_s)
