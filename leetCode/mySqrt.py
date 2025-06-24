class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 1
        while True : 
            if x / i ** 2 < 1 :
                return i-1
            elif x / i ** 2 == 1 : return i             
            else : i += 1
