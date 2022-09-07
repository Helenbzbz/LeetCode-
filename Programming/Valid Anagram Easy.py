# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_dict = {}
#         for i in s:
#             if i in s_dict.keys(): 
#                 s_dict[i] = s_dict[i]+1
#             else: s_dict[i] = 1
#         t_dict = {}  
#         for i in t:
#             if i in t_dict.keys(): t_dict[i] = t_dict[i]+1
#             else: t_dict[i] = 1
                
#         for t in t_dict.keys():
#             if t not in s_dict.keys(): return False
#             elif t_dict[t] != s_dict[t]: return False
            
#         for s in s_dict.keys():
#             if s not in t_dict.keys(): return False
#             elif s_dict[t] != t_dict[t]: return False
            
#         return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
    
        s_dict = {}
        for i in s:
            if i in s_dict.keys(): 
                s_dict[i] = s_dict[i]+1
            else: s_dict[i] = 1
                
        for i in t:
            if i in s_dict.keys() and s_dict[i]>0: s_dict[i] = s_dict[i]-1
            else: return False
        
        return sum(s_dict.values()) == 0
