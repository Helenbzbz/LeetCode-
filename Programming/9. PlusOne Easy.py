class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_list = []
        new_num = digits[-1]+1
        
        if new_num >= 10:
            unit_num = new_num -10
            digits[-1] = unit_num
            above_10 = 1
            for i in reversed(range(0,len(digits)-1)):
                new_num = above_10+digits[i]
                if new_num <10:
                    digits[i] = new_num
                    above_10 = 0
                    break
                else:
                    digits[i] = new_num-10
                    above_10 = 1
            if above_10 == 1:
                digits.insert(0,1)
             
        else:
            digits[-1] = new_num
        return digits

## Instead of doing plus, we don't need the actual number, cause we only + 1, the fact that a digit is 9 and there is an leftover is enough for determining the values
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lastCarry = None
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
                lastCarry = i
            else:
                digits[i] += 1
                break
        if lastCarry == 0:
            digits.insert(0, 1)
        return digits
    
