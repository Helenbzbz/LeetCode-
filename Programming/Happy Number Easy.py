# For any cycle, we either: 1. get to 1; 2. stuck in a cycle; 3. goes to infinity
# So we need two functions, first is find next number after calculation, second check if the result already appears or n=1

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def calculate_next(n):
            result = 0
            while n > 0:
                last_digit = n%10
                n = floor(n/10)
                result = last_digit**2+result
            return result
                
        appeared = set()
        while n!= 1 and n not in appeared:
            appeared.add(n)
            n = calculate_next(n)
        
        return n == 1
