class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        cur_size = 0
        total_unit = 0
        
        boxTypes.sort(key = lambda x: -x[1])
        
        
        for num_box, unit in boxTypes:
            total_unit += unit*min(truckSize - cur_size, num_box)
            cur_size += min(truckSize - cur_size, num_box)
        return total_unit
