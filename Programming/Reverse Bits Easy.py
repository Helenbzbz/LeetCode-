class Solution:
    def reverseBits(self, n: int) -> int:
        power = 31
        result = 0
        while n > 0:
            digit = n%2
            n = floor(n/2)
            result = result + digit*(2**power)
            power -=1
        return result
            
