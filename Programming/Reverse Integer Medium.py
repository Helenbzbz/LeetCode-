# My intuition though is to get rid of number one by one in x and then move it to another integer
class Solution:
    def reverse(self, x: int) -> int:
        reverse_int = 0
        ten_count = 1
        decimal_count = 0
        negative_count = 1
        if x <0: 
            x = -x
            negative_count = -1
        while x >0:
            unit_digit = x%10
            x = floor(x/10)
            reverse_int += unit_digit*ten_count
            ten_count = ten_count/10
            decimal_count+=1
     
        reverse_value = (reverse_int*(10**(decimal_count-1)))*negative_count
        if reverse_value > 2**31-1: return 0
        elif reverse_value < (-2)**31: return 0
        return round(reverse_value)
