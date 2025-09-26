class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        answer = 0

        for i in range(len(prices)) : 
            stdPrice = prices[i]
            
            if minPrice > stdPrice :
                minPrice = stdPrice
            else : 
                answer = max(answer, stdPrice - minPrice)    
        
        return answer
