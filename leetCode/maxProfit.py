class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        maxProfit = 0

        for price in prices : 
            if minPrice > price :
                minPrice = price
            else : 
                answer = max(maxProfit, price - minPrice)    
        
        return maxProfit
