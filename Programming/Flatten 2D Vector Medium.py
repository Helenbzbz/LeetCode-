class Vector2D:

    def __init__(self, vec: List[List[int]]):
        sorted_vec = []
        for i in vec:
            for num in i:
                sorted_vec.append(num)
        self.vec = sorted_vec
        self.next_index = 0

    def next(self) -> int:
        self.next_index += 1
        return self.vec[(self.next_index-1)]

    def hasNext(self) -> bool:
        if self.next_index > len(self.vec)-1: return False
        return True


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
