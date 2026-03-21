def hammingWeight(self, n: int) -> int:
        binN = bin(n)[2:]
        #print(binN)
        binList = list(binN)
        #print(binList)
        answer = 0

        for i in binList:
            if i == '1' :
                answer += 1
        
        return answer
