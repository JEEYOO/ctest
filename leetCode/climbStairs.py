class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1 or n == 2 : return n
        else : 
            a, b = 1, 2
            for whatever in range(3, n+1):
                a, b = b, a + b

            return b
          
#return self.climbStairs(n-1) + self.climbStairs(n-2)
