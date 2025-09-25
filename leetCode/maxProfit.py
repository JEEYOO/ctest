class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        answer = 0

        for i in range(len(prices)) : 
            stdPrice = prices[i]
               
            for each in prices[i:] : 
                if answer < each - stdPrice :
                    answer = each - stdPrice    
        
        return answer
