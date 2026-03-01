class Solution:
    def reverseBits(self, n: int) -> int:
        
        binaryN = str(bin(n)[2:]) #0011
        
        #binary32 = f"{binaryN:32}"
        binary32 = binaryN.zfill(32)
        
        

        listN = list(binary32)
        listN.reverse()
        #reversed
 
        answer = ''
        
        
        for each in listN:
            answer += each
        
        
        

        return int(answer, 2)
