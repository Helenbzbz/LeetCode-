left = ['(','[','{']
right = [')',']','}']

class Solution:
    def isValid(self, s: str) -> bool:
        store = []
        for letter in s:
            if letter in left:
                store.append(letter)
            elif letter in right:
                if store == []:
                    return False
                if left.index(store.pop())!= right.index(letter):
                    return False
        return len(store) == 0
       
