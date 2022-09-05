## The palindromic string is the one when read from left equals to read from right
## My original though was to have two points moving from left and right -> this is not right as this can only identify the string that's center in the middle
## What I should do instead is to have 2 pointers expanding from each center -> we don't need to store every single one, whenever we have it we do a comparision with the last one and we can just keep the longer one

## This is force listing method
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         m = ''
#         for i in range (len(s)):
#             for j in range(len(s),i,-1):
#                 if len(m) >= j-i:
#                     break
#                 elif s[i:j] == s[i:j][::-1]:
#                     m = s[i:j]
#                     break
#         return m

class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''
        for i in range (len(s)):
            lp = 0
            rp = 0
            while lp <= i and rp +i < len(s) and s[i-lp] == s[i+rp]:
                lp += 1
                rp += 1
            if len(m) < lp+rp-1:
                m = s[(i-lp+1):(i+rp)]
        
        for i in range (len(s)):
            lp = 0
            rp = 1
            while lp <= i and rp +i < len(s) and s[i-lp] == s[i+rp]:
                lp += 1
                rp += 1
            if len(m) < lp+rp-1:
                m = s[(i-lp+1):(i+rp)]
        
        return m
