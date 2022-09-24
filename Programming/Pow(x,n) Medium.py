class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if x == 1: return 1
        if x == -1: return 
        current_number = 1
        if n > 0:
            while n>0:
                current_number = current_number*x
                n-=1
        if n < 0:
            while n<0:
                current_number = current_number/x
                n+=1
        return current_number
