class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        answer = 0

        for i in range(len(prices)) : 
            stdPrice = prices[i]
            maxP = max(prices[i:])
            
            if answer < maxP - stdPrice :
                answer = maxP - stdPrice    
        
        return answer
