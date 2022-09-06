# One way is to do force listing but it's gonna to be super slow
# I think we can keep two index in a list, we move the buy point from middle and gradually move towards the center and one point for sell and gradually move towards middle?

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        for i in prices:
            if i < min_price: 
                min_price = i
            elif profit < i -min_price: 
                profit = i -min_price
        return profit

# Tip: if you can directly refer to item, does not use indexing
