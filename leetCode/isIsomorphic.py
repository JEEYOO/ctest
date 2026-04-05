def isIsomorphic(self, s: str, t: str) -> bool:

        listS = list(s)
        listT = list(t)
        
        dictC = dict()     
        
        num = 0
        for alpha in listS : 
            if alpha not in dictC :
                dictC[alpha] = listT[num]
            elif dictC[alpha] != listT[num]:
                return False 
            else : 
                pass
            num += 1
        
        dictD = dict()     

        num2 = 0
        for beta in listT : 
            if beta not in dictD :
                dictD[beta] = listS[num2]
            elif dictD[beta] != listS[num2]:
                return False 
            else : 
                pass
            num2 += 1
        
        
        return True
        
        
