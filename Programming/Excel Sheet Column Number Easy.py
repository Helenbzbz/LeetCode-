# This is from Right to Left
# class Solution:
#     def titleToNumber(self, columnTitle: str) -> int:
#         charactor_dict = {
#             'A':1, 'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11, 'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26
#         }
#         i = len(columnTitle)-1
#         count = 1
#         result = 0
#         while i>=0:
#             result += count*charactor_dict[columnTitle[i]]
#             i -= 1
#             count = count *26
#         return result

# We can do it from Left to right also in a way don't need the dictionary is to use ord(str) - ord(str)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        n = len(columnTitle)
        i = 0
        while i <n:
            result = result*26
            result += (ord(columnTitle[i])-ord('A')+1)
            i+=1
        return result
