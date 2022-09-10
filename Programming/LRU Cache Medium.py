## We can either use OrderedDict package
## Or, in Python, the key-value pairs are stored in order -> we can use pop() and then redefine by dict['key'] = dict.pop('key')


# from collections import OrderedDict
# class LRUCache(OrderedDict):

#     def __init__(self, capacity: int):
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key in self:
#             self.move_to_end(key)
#             return self[key]
#         else:
#             return -1
        

#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#             self[key] = value
#         else:
#             if len(self) < self.capacity:
#                 self[key] = value
#             else:
#                 self.popitem(last = False)
#                 self[key] = value
     

class LRUCache(dict):
    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self:
            self[key] = self.pop(key)
            return self[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self:
            del self[key]
            self[key] = value
        else:
            if len(self) < self.capacity:
                self[key] = value
            else:
                self.pop(list(self.keys())[0])
                self[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
