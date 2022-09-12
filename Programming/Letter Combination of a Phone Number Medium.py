class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_char = {'1':'','2':'abc','3':'def','4':'ghi',
                       '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result = []
        if digits == '': return result
        i = 0
        
        while i< len(digits):
            digit = digits[i]
            i+=1
            
            new_list = []
            for char in number_char[digit]:
                if i == 1:
                    new_list.append(char)
                else:
                    for word in result:
                        new_list.append(word+char)
            result = new_list.copy()
            new_list = []
            
        return result
