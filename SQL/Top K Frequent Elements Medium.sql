class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)
        
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        # Counter takes an iterable (such as a string, a list, or a dict object) and gives the object counts as long as the objects are hashable
        
        return heapq.nlargest(k, count.keys(), key=count.get)
        # Count.get -> sort by key is the count.get
