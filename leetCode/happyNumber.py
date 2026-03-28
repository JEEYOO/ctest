def isHappy(self, n: int) -> bool:
        
        #strN = str(n)
        #print(list(strN))
        listN = list(str(n))
        
        while ckNum != 1 : # len(listN) != 1  : #1 and int(listN[0])**2 > 10
            ckNum = 0
            for each in listN : #1,0
                ckNum += int(each)**2

            if ckNum == 1:
                return True
            else : 
                listN = list(str(ckNum)) 
        
        if listN[0] == '1':
            return True
        else : return False


        '''
        while True : 
            if (n / 10 != 0) : 
                tempNum += (n / 10)**2
                n = 
            else : 
                tempNum += (n % 10)**2
        '''
