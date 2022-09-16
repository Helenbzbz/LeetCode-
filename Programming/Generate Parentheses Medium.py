## This is by Brute Force :) We can have a better way
class Solution(object):
    def generateParenthesis(self, n):   
    # The logic of this function, if length of A is already 2*n, then we can check if valid, if valid we will add this into the answer
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
    # else, we first append a (, then generate (A) -> take us to append '(', then continously, then do a judement; if fail, we pop and add ), if fail, we pop this and get out of this generate A to append ) -> if both fail, we will get out and start with (((((.
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

    # The logic of valid function is we keep track of balance, when we found ( then the count will increase by 1 if it's ) then balance -1, and as soon as the balance is <-1 then return False.
    # Lesson learnt! Don't look at algorithms in the way of human sannning!!! Algorithm read differently from you did.
        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0
        ans = []
        generate()
        return ans
    
## Instead of add ( or ) everytime, only add when we know it's still valid
## You have learn how to call function within a function !! :(
class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2*n:
                ans.append("".join(S))
                return
            if left <n:
                S.append("(")
                backtrack(S,left+1,right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
