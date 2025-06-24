class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sumAB = self.biToInt(a) + self.biToInt(b)
                    #3
        print(sumAB)
        return self.intToBi(sumAB)

    def biToInt(self, c: str) -> int:
        num = 0
        listC = list(c) #1, 0, 1, 0
        for i in range(len(listC)-1, -1, -1): 
                        #    3
            num += int(listC[len(listC)-i-1]) * (2 ** i)

        return num

    def intToBi(self, d: int) -> str:
        seung = 0 
        m = 0
        while True : #INFINITE?
            
            if d // 2 ** m == 1 :  #4
                seung = m
                break
            else : m += 1
        
        strBi = ""
        for i in range(seung, -1, -1):
                        #4
            left = d % (2 ** i)
           #1     5  4
            strBi += str(d // 2 ** i)
           #1            21   16
            d = left

        return strBi
