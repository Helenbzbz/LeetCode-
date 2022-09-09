# Operation that has O(1) as time complexity:
# In Python, we can use hashmap or array list, array list has indexes -> has issue with delete so we might need to use swap & delete. Dict.ketys() in python 3 has time complexity of O(1)

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        
    def insert(self, val: int) -> bool:
        if val in self.dict: 
            return False
        else: 
            self.dict[val] = 1 
            return True
        
    def remove(self, val: int) -> bool:
        if val in self.dict.keys(): 
            del self.dict[val]
            return True
        else: 
            return False

    def getRandom(self) -> int:
        a = self.dict.keys()
        return choice(list(self.dict.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
